import json
import yaml


YML = ('.yml', '.yaml')


def process_to_python_format(file_path1, file_path2):
    for file_path in file_path1, file_path2:
        if file_path.endswith('.json'):
            if file_path == file_path1:
                file1 = json.load(open(file_path))
            if file_path == file_path2:
                file2 = json.load(open(file_path))
        if file_path.endswith(YML):
            if file_path == file_path1:
                file1 = yaml.full_load(open(file_path))
            if file_path == file_path2:
                file2 = yaml.full_load(open(file_path))
    return file1, file2
