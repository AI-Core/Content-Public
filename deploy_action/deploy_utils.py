import requests
import json
import os
import yaml
import glob

class PathHelper:
    def __init__(self, unit):
        self.unit = unit


    def get_meta(self, filepath, type):
        '''
        Returns the metadata for a file stored in a yaml file.

        '''
        file = os.path.join(filepath, f'.{type}.yaml')
        with open(file) as f:
            meta = yaml.safe_load(f)
        return meta


    def get_module_paths(self):
        not_modules = [
            ".git",
            ".idea",
            ".tox",
            "__pycache__",
            ".vscode",
            "Project Briefs",
            "Extra",
        ]
        not_modules = [os.path.join(self.unit, m) for m in not_modules]
        return [
            p
            for p in glob.glob(f'{self.unit}/*')
            if os.path.isdir(p) and p[0] != "." and p not in not_modules
        ]


    def get_lesson_paths(self):
        paths = []
        modules = self.get_module_paths()
        for module_path in modules:
            lesson_paths = self._get_lesson_paths_in_module(module_path)
            paths.extend(lesson_paths)
        return paths


    def get_quiz_paths(self):
        lesson_folder_paths = self.get_lesson_paths()
        quizz_paths = []
        for lesson_folder_path in lesson_folder_paths:
            quizz_paths.append(self._get_quiz_path_in_lesson(lesson_folder_path))
        return quizz_paths


    def get_challenge_paths(self):
        lesson_folder_paths = self.get_lesson_paths()
        challenge_paths = []
        for lesson_folder_path in lesson_folder_paths:
            challenge_paths.append(self._get_challenges_path_in_lesson(lesson_folder_path))
        return challenge_paths
    
    def get_study_guide_paths(self):
        lesson_folder_paths = self.get_lesson_paths()
        study_guide_paths = []
        for lesson_folder_path in lesson_folder_paths:
            study_guide_paths.append(self._get_study_guides_path_in_lesson(lesson_folder_path))
        return study_guide_paths


    def get_lesson_paths_in_module(self, module_path):
        not_lessons = [
            ".git",
            ".idea",
            ".tox",
            "__pycache__",
            ".vscode",
            "Project Briefs",
            "Extra",
        ]
        lesson_names = [m for m in os.listdir(module_path) if m[0] != "." and m not in not_lessons]
        lesson_names = [
            ln for ln in lesson_names if os.path.isdir(os.path.join(module_path, ln))
        ]
        lesson_paths = []
        for lesson in lesson_names:
            if lesson == "Extra" or lesson == "images":
                continue
            path = os.path.join(module_path, lesson)
            lesson_paths.append(path)
        
        lesson_paths = sorted(lesson_paths, key=self.__get_lesson_idx_from_path)
        return lesson_paths

    @staticmethod
    def get_study_guide_path_in_lesson(lesson_path):
        study_guides_path = os.path.join(lesson_path, "Study Guide.md")
        if os.path.isfile(study_guides_path):
            return study_guides_path
        else:
            print(f'There is no Study Guide in {" - ".join(lesson_path.split("/")[1:])}')
            return 'None'
    
    @staticmethod
    def get_notebook_path_in_lesson(lesson_path):
        notebook_path = os.path.join(lesson_path, "Notebook.ipynb")
        if os.path.isfile(notebook_path):
            return notebook_path
        else:
            print(f'There is no Notebook in {" - ".join(lesson_path.split("/")[1:])}')
            return 'None'
    
    @staticmethod
    def get_challenge_path_in_lesson(lesson_path):
        challenge_path = os.path.join(lesson_path, ".challenges.yaml")
        if os.path.isfile(challenge_path):
            return challenge_path
        else:
            print(f'There is no challenge in {" - ".join(lesson_path.split("/")[1:])}')
            return 'None'

    @staticmethod
    def get_quiz_path_in_lesson(lesson_path):
        quiz_path = os.path.join(lesson_path, ".quiz.yaml")
        if os.path.isfile(quiz_path):
            return quiz_path
        else:
            print(f'There is no quiz in {" - ".join(lesson_path.split("/")[1:])}')
            return 'None'

    @staticmethod
    def __get_lesson_idx_from_path(lesson_path):
        lesson_name = lesson_path.split('/')[-1]
        idx = int(lesson_name.split('.')[0])
        return idx


class RequestHelper:

    def __init__(self, API_ROOT):
        self.API_ROOT = API_ROOT

    def create_or_update_unit(self, unit_meta):
        self._request(f"{self.API_ROOT}/content/unit", unit_meta)

    def create_or_update_module(self, module_meta):
        self._request(f"{self.API_ROOT}/content/module", module_meta)

    def create_or_update_lesson(self, lesson_meta):
        self._request(f"{self.API_ROOT}/content/lesson", lesson_meta)

    def create_or_update_quiz(self, quiz):
        self._request(f"{self.API_ROOT}/content/quiz", quiz)

    def create_or_update_challenge(self, challenge):
        self._request(f"{self.API_ROOT}/content/challenge", challenge)

    def set_prerequisites(self, module_id: str, prerequisite_module_ids: list):
        """Deletes existing prerequisites for module with id equal to `module_id` and assigns new ones equal to ids in `prerequisite_module_ids`"""
        self._request(f"{self.API_ROOT}/content/module/prerequisites", {
            'module_id': module_id,
            'prerequisite_module_ids': prerequisite_module_ids
        })

    def _request(self, url, payload_yaml):
        response = requests.post(url, data=json.dumps(payload_yaml))
        assert response.status_code == 200, f"{response.status_code} - {response.text}"