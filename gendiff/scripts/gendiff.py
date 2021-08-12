#!/usr/bin/env python
import argparse
parser = argparse.ArgumentParser(description='Generate diff')
parser.add_argument("first_file", help="first file for comparison")
parser.add_argument("second_file", help="second file for comparison")
parser.add_argument("-f", "--format", default='json', help="set format of output")
args = parser.parse_args()
