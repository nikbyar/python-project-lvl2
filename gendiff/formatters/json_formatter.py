import json
from gendiff.formatters.stylish_formatter import make_stylish


def make_json(pre_diff):
    return json.dumps(make_stylish(pre_diff))
