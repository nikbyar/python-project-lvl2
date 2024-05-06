from gendiff.pre_diff_maker import generate_pre_diff
from gendiff.formatters.plain_formatter import make_plain
from gendiff.formatters.stylish_formatter import make_stylish
from gendiff.formatters.json_formatter import make_json
from gendiff.data_parser import parse
from gendiff.format_determiner import determine_format


def generate_diff(first_file, second_file, file_format='stylish'):
    parsed_file1 = parse(first_file, determine_format(first_file))
    parsed_file2 = parse(second_file, determine_format(second_file))
    pre_diff = generate_pre_diff(parsed_file1, parsed_file2, {})
    if file_format == 'plain':
        return make_plain(pre_diff)
    elif file_format == 'stylish':
        return make_stylish(pre_diff)
    elif file_format == 'json':
        return make_json(pre_diff)
