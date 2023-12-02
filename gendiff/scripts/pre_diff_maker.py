import json
import yaml


def load_json(file_path):
    return json.load(open(file_path))


def load_yaml(file_path):
    return yaml.safe_load(open(file_path))


def define_format(file):
    if file.endswith('.json'):
        file = load_json(file)
    elif file.endswith('.yaml') or file.endswith('.yml'):
        file = load_yaml(file)
    return file


def generate_pre_diff(file1, file2):
    file1 = define_format(file1)
    file2 = define_format(file2)

    diff = {}

    def inner(file1, file2, merged_dict):
        all_keys = file1.keys() | file2.keys()

        for key in sorted(all_keys):
            if key not in file1.keys():
                merged_dict[key] = ['added', file2.get(key)]
            elif key not in file2.keys():
                merged_dict[key] = ['deleted', file1.get(key)]
            elif file1[key] == file2[key]:
                merged_dict[key] = ['unchanged', file1.get(key)]
            else:
                merged_dict[key] = ['changed']
                if isinstance(file1.get(key), dict) and \
                        isinstance(file2.get(key), dict):
                    merged_dict[key].append({})
                    inner(file1.get(key), file2.get(key), merged_dict[key][1])
                else:
                    merged_dict[key] += [file1.get(key), file2.get(key)]
    inner(file1, file2, diff)
    return diff
