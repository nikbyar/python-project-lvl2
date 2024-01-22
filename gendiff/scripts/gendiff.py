from gendiff.parser import get_parser
from gendiff.format_selector import select_format


def main():
    first_file, second_file, file_format = get_parser()
    print(select_format(first_file, second_file, file_format))


if __name__ == '__main__':
    main()
