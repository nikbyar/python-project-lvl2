from gendiff.scripts.parser import get_parser
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


def generate_diff_(file1, file2):
    file1 = define_format(file1)
    file2 = define_format(file2)
    diff = ''
    for key in sorted(file1 | file2):
        if key not in file1:
            diff = diff + f'  + {key}: {file2[key]}\n'
        elif key not in file2:
            diff = diff + f'  - {key}: {file1[key]}\n'
        elif file1[key] != file2[key]:
            diff = diff + f'  - {key}: {file1[key]}\n' + \
                f'  + {key}: {file2[key]}\n'
        else:
            diff = diff + f'    {key}: {file1[key]}\n'
    diff = f'{{\n{diff}}}'
    return diff


def generate_diff_nested(file1, file2):
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


def build_diff_tree(pre_diff):
    SPACES = '    '
    SPACES_PLUS = '  + '
    SPACES_MINUS = '  - '

    def walk(value, diff, depth):
        if isinstance(value, dict):
            diff = '{'
            for key in value.keys():
                if not isinstance(value[key], list):
                    if isinstance(value[key], dict):
                        diff += f'\n{SPACES * depth}{key}: '
                        diff += walk(value[key], diff, depth + 1)
                    elif not isinstance(value[key], dict):
                        diff += f'\n{SPACES * depth}{key}: {value[key]}'

                elif value[key][0] == 'changed' and len(value[key]) == 2:
                    diff += f'\n{SPACES * depth}{key}: '
                    diff += walk(value[key][1], diff, depth + 1)
                elif value[key][0] == 'changed' and len(value[key]) == 3:
                    diff += f'\n{SPACES * (depth - 1) + SPACES_MINUS}{key}: '
                    diff += walk(value[key][1], diff, depth + 1)
                    diff += f'\n{SPACES * (depth - 1) + SPACES_PLUS}{key}: '
                    diff += walk(value[key][2], diff, depth + 1)
                elif value[key][0] == 'added' \
                        and isinstance(value[key][1], dict):
                    diff += f'\n{SPACES * (depth - 1) + SPACES_PLUS}{key}: '
                    diff += walk(value[key][1], diff, depth + 1)
                elif value[key][0] == 'added' \
                        and not isinstance(value[key][1], dict):
                    diff += f'\n{SPACES * (depth - 1) + SPACES_PLUS}{key}: ' \
                            f'{value[key][1]}'
                elif value[key][0] == 'deleted' \
                        and isinstance(value[key][1], dict):
                    diff += f'\n{SPACES * (depth - 1) + SPACES_MINUS}{key}: '
                    diff += walk(value[key][1], diff, depth + 1)
                elif value[key][0] == 'deleted' \
                        and not isinstance(value[key][1], dict):
                    diff += f'\n{SPACES * (depth - 1) + SPACES_MINUS}{key}: ' \
                            f'{value[key][1]}'
                elif value[key][0] == 'unchanged':
                    diff += f'\n{SPACES * depth}{key}: {value[key][1]}'
        if not isinstance(value, dict):
            return str(value)
        diff += f'\n{SPACES * (depth - 1)}}}'
        return diff
    return walk(pre_diff, ' ', 1)


def build_diff_plain(pre_diff):
    def walk(value, diff, path):
        diff = ""
        if isinstance(value, dict):
            for key in value.keys():
                if not isinstance(value[key], list):
                    if isinstance(value[key], dict):
                        walk(value[key], diff, path + key + '.')
                elif value[key][0] == 'changed' and len(value[key]) == 2:
                    diff += walk(value[key][1], diff, path + key + '.')
                elif value[key][0] == 'changed' and len(value[key]) == 3:
                    prev_value = f"'{value[key][1]}'"
                    new_value = f"'{value[key][2]}'"
                    if isinstance(value[key][1], dict):
                        prev_value = '[complex value]'
                    if isinstance(value[key][2], dict):
                        new_value = '[complex value]'
                    diff += f"Property '{path}{key}' was updated. From {prev_value} to {new_value}\n"
                elif value[key][0] == 'added' \
                        and isinstance(value[key][1], dict):
                    diff += f"Property '{path}{key}' was added with value: [complex value]\n"
                elif value[key][0] == 'added' \
                        and not isinstance(value[key][1], dict):
                    diff += f"Property '{path}{key}' was added with value: '{value[key][1]}'\n"
                elif value[key][0] == 'deleted':
                    diff += f"Property '{path}{key}' was removed\n"
        if not isinstance(value, dict):
            return str(value)
        return diff
    return '\n' + walk(pre_diff, '', '')


def replace_stylish(diff):
    return diff.replace('False', 'false').replace('None', 'null').\
        replace('True', 'true')


def replace_plain(diff):
    return diff.replace("'False'", 'false').replace("'None'", 'null').\
        replace("'True'", 'true').rstrip()


def stylish(file1, file2):
    pre_diff = generate_diff_nested(file1, file2)
    return replace_stylish(build_diff_tree(pre_diff))


def plain(file1, file2):
    pre_diff = generate_diff_nested(file1, file2)
    return replace_plain(build_diff_plain(pre_diff))


def main():
    first_file, second_file = get_parser()
    pre_diff = generate_diff_nested(first_file, second_file)
    print(replace_stylish(build_diff_tree(pre_diff)))


if __name__ == '__main__':
    first_file, second_file = get_parser()
    plain(first_file, second_file)
