import json
import yaml


YML = ('.yml', '.yaml')


def process_to_python_format(file_path1, file_path2):
    if file_path1.endswith('.json') and file_path2.endswith('.json'):
        file1 = json.load(open(file_path1))
        file2 = json.load(open(file_path2))
    if file_path1.endswith(YML) and file_path2.endswith(YML):
        file1 = yaml.full_load(open(file_path1))
        file2 = yaml.full_load(open(file_path2))
    return file1, file2
