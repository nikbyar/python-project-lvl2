#!/usr/bin/env python
from gendiff.gendiff_json import generate_diff_json
from gendiff.gendiff_yml import generate_diff_yml
from gendiff.parser import parse_files
import argparse


YML = ('.yml', '.yaml')


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument("first_file", help="first file for comparison")
    parser.add_argument("second_file", help="second file for comparison")
    parser.add_argument("-f", "--format", default='json', help="set format of output") # noqa
    args = parser.parse_args()
    if args.first_file.endswith('.json') and args.second_file.endswith('.json'):
        file1, file2 = generate_diff_json(args.first_file, args.second_file)
    if args.first_file.endswith(YML) and args.second_file.endswith(YML):
        file1, file2 = generate_diff_yml(args.first_file, args.second_file)
    print(parse_files(file1, file2))


if __name__ == '__main__':
    main()
