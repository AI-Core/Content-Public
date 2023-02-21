import yaml
import os
from typing import List
import nbformat

yaml_file = 'practicals.yaml'
with open(yaml_file, 'r') as f:
    practical_list: List[dict] = yaml.safe_load(f)

if practical_list:
    os.makedirs('Practicals', exist_ok=True)

for idx, practical in enumerate(practical_list):
    # Create a new subdirectory for each practical
    practical_name = practical.pop('name')
    new_folder = f"{idx}. {practical_name}"
    os.makedirs(os.path.join('Practicals', new_folder), exist_ok=True)

    # Create a new specifications.yaml file for each practical
    with open(os.path.join('Practicals', new_folder, 'specifications.yaml'), 'w') as f:
        yaml.dump(practical, f, sort_keys=False)
    
    description = practical.pop('description')

    # Create a new notebook for each practical
    with open(os.path.join('Practicals', new_folder, 'Practical.ipynb'), 'w') as f:
        nb = nbformat.v4.new_notebook()
        # Add a title cell
        nb.cells.append(nbformat.v4.new_markdown_cell(f'# {practical_name}'))
        # For each line in the description, add a new markdown cell with 4 #s
        for line in description.splitlines():
            if len(line) == 0:
                continue
            nb.cells.append(nbformat.v4.new_markdown_cell(f'#### {line}'))
            # Add an empty code cell with the code between lines
            nb.cells.append(nbformat.v4.new_code_cell(''))
        nbformat.write(nb, f)