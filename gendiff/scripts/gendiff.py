import argparse
import json


parser = argparse.ArgumentParser(
    description='Compares two configuration files and shows a difference.')
a = parser.add_argument('first_file')
b = parser.add_argument('second_file')
parser.add_argument('-f', '--format', help='set format of output')
args = parser.parse_args()

first_file = args.first_file
second_file = args.second_file


def load_json(file1_path, file2_path):
    return json.load(open(file1_path)), json.load(open(file2_path))


def generate_diff(file1, file2):
    file1, file2 = load_json(file1, file2)
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
    print(generate_diff(first_file, second_file))


if __name__ == '__main__':
    main()
