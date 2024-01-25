from gendiff.format_selector import select_format


def generate_diff(first_file, second_file, file_format='stylish'):
    return select_format(first_file, second_file, file_format)
