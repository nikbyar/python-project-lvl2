from gendiff.pre_diff_maker import generate_pre_diff
from gendiff.formatters.plain_formatter import make_plain
from gendiff.formatters.stylish_formatter import make_stylish
import json


def select_format(first_file, second_file, file_format='stylish'):
    pre_diff = generate_pre_diff(first_file, second_file)
    if file_format == 'plain':
        return make_plain(pre_diff)
    elif file_format == 'stylish':
        return make_stylish(pre_diff)
    elif file_format == 'json':
        return json.dumps(make_stylish(pre_diff))
