from gendiff.parser import get_parser
from gendiff.format_selector import select_format


def generate_diff():
    first_file, second_file, file_format = get_parser()
    return select_format(first_file, second_file, file_format)


def main():
    print(generate_diff())


if __name__ == '__main__':
    main()
