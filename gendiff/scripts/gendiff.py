import argparse
import json
import yaml


def get_parser():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    first_file = args.first_file
    second_file = args.second_file
    return first_file, second_file


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


def generate_diff(file1, file2):
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


def main():
    first_file, second_file = get_parser()
    print(generate_diff(first_file, second_file))


if __name__ == '__main__':
    main()
