#!/usr/bin/env python
from gendiff.gendiff import generate_diff
import argparse





def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument("first_file", help="first file for comparison", type=str)
    parser.add_argument("second_file", help="second file for comparison", type=str)
    parser.add_argument("-f", "--format", default='json', help="set format of output")
    args = parser.parse_args()
    generate_diff(args.first_file, args.second_file)

    

if __name__ == '__main__':
    main()