from deploy_utils import PathHelper
from deploy_utils import RequestHelper
import glob
import os
import sys
import yaml
import urllib

def read_input() -> str:
    '''
    Reads the argument passed through the command line

    Returns:
    --------
    units: str
        The name of the unit folder passed through the command line
        If no argument is passed, the default value is "*" corresponding to all units
    '''
    if len(sys.argv) == 1:
        print("Deploying the content for all the units")
        units = '*'
    elif len(sys.argv) == 2:
        print(f'Deploying content for the {sys.argv[1]} unit')
        units = sys.argv[1]
    else:
        print("Invalid number of arguments")
        exit(1)
    return units


def get_unit_folder() -> dict:
    '''
    Returns a dictionary for all the units specified in the command line

    Returns:
    --------
    pathways: dict
        A dictionary with the name of the unit as the key and another dictionary as the value
        The nested dictionary has the following keys:
        - "Modules": a list of all the modules in the unit
        - "Lessons": a list of all the lessons in the unit
        - "Quizzes": a list of all the quizzes in the unit
        - "Challenges": a list of all the challenges in the unit
        - "Study Guides": a list of all the study guides in the unit
    '''
    units = glob.glob(read_input())
    if len(units) == 0:
        print("No units found, did you specify the correct unit?")
        exit(1)
    units = [u for u in units if u not in path_ignore_list]
    pathways = {unit: {} for unit in units}
    return pathways


def get_all_paths(pathways):
    for unit in pathways:
            print(f'Getting paths for {unit}')
            path_helper = PathHelper(unit)
            module_paths = path_helper.get_module_paths()
            pathways[unit] = {m_path: {}
                                    for m_path in module_paths}
            for module_path in pathways[unit]:
                lesson_paths = path_helper.get_lesson_paths_in_module(module_path)
                pathways[unit][module_path] = {l_path: {
                                    'Quiz': '',
                                    'Challenge': '',
                                    'Study Guide': '',
                                    'Notebook': ''} for l_path in lesson_paths
                }

                for lesson_path in pathways[unit][module_path]:
                    pathways[unit][module_path][lesson_path]['Quiz'] = path_helper.get_quiz_path_in_lesson(lesson_path)
                    pathways[unit][module_path][lesson_path]['Challenge'] = path_helper.get_challenge_path_in_lesson(lesson_path)
                    pathways[unit][module_path][lesson_path]['Study Guide'] = path_helper.get_study_guide_path_in_lesson(lesson_path)
                    pathways[unit][module_path][lesson_path]['Notebook'] = path_helper.get_notebook_path_in_lesson(lesson_path)
    return pathways


def get_elements_in_lesson(lesson_path):
    quiz = lesson_path['Quiz']
    challenge = lesson_path['Challenge']
    study_guide = lesson_path['Study Guide']
    notebook = lesson_path['Notebook']
    return quiz, challenge, study_guide, notebook


path_ignore_list = [
    "deploy_action",
    "test.ipynb",
]

API_ROOT = os.environ['API_ROOT']
content_repo = 'AI-Core/Content-Public'

if __name__ == "__main__":
    requester = RequestHelper(API_ROOT)
    pathways = get_unit_folder()
    # Fill the dictionary with all the directories, so if a directory is missing, the workflow will stop and exit
    pathways = get_all_paths(pathways)
    for unit in pathways:
        path_helper = PathHelper(unit)
        unit_meta = path_helper.get_meta(unit, 'unit')
        print(f'Updating unit {unit}')
        requester.create_or_update_unit(unit_meta)
        for module_path in pathways[unit]:
            module_meta = path_helper.get_meta(module_path, 'module')
            if 'prerequisites' in module_meta:
                prerequisite_module_ids = module_meta.pop('prerequisites') # pop off
                prerequisite_module_ids = [p['id'] for p in prerequisite_module_ids]
                # CREATE ROW IN PREREQUISITES TABLE
                print(f'\tUpdating prerequisites for module {module_path.split("/")[-1]}')
                requester.set_prerequisites(module_meta['id'], prerequisite_module_ids)
            module_meta["name"] = module_path.split("/")[-1]
            module_meta["unit_id"] = unit_meta["id"]
            print(f'\tUpdating module {module_path.split("/")[-1]}')
            requester.create_or_update_module(module_meta)
            for lesson_idx, lesson_path in enumerate(pathways[unit][module_path]):
                quiz, challenge, study_guide, notebook = get_elements_in_lesson(pathways[unit][module_path][lesson_path])

                lesson_meta = path_helper.get_meta(lesson_path, "lesson")
                lesson_name = lesson_path.split("/")[-1]

                try:
                    lesson_name = lesson_name.split(". ")[1]
                except:
                    print(
                        f"WARNING: {lesson_name} was expected to be numbered and contain '. ', but didn't"
                    )
                lesson_meta["name"] = lesson_name
                lesson_meta["idx"] = lesson_idx
                lesson_meta["module_id"] = module_meta["id"]
                requires_notebook = True
                if "requires_notebook" in lesson_meta:
                    requires_notebook = lesson_meta.pop(
                        "requires_notebook"
                    ) 
                # If there is a quiz, add it to the lesson
                if quiz != 'None':
                    with open(quiz) as f:
                        quiz = yaml.safe_load(f)
                    quiz["lesson_id"] = lesson_meta["id"]

                if notebook != 'None':
                    colab_link = f"https://colab.research.google.com/github/{content_repo}/blob/main/{notebook}"
                    colab_link = urllib.parse.quote(colab_link, safe="%/:")
                    lesson_meta["notebook_url"] = colab_link

                if study_guide != 'None':
                    with open(study_guide, "r") as f:
                        lesson_meta["study_guide"] = f.read()

                if challenge != 'None':
                    with open(challenge, "r") as f:
                        challenges = yaml.safe_load(f)
                    for challenge_idx, challenge in enumerate(challenges):
                        challenge["lesson_id"] = lesson_meta["id"]
                        challenge["idx_in_lesson"] = challenge_idx
                        requester.create_or_update_challenge(challenge)
                
                print(f'\t\tUpdating lesson {lesson_name}')
                requester.create_or_update_lesson(lesson_meta)
                