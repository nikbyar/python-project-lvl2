#!/usr/bin/env python
from gendiff.processor import process_to_python_format
from gendiff.parser import parse_files
import argparse


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument("first_file", help="first file for comparison")
    parser.add_argument("second_file", help="second file for comparison")
    parser.add_argument("-f", "--format", default='json', help="set format of output") # noqa
    args = parser.parse_args()
    file1, file2 = process_to_python_format(args.first_file, args.second_file)
    print(parse_files(file1, file2))


if __name__ == '__main__':
    main()
