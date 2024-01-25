from gendiff.parser import get_parser
from gendiff.gendiff import generate_diff


def main():
    first_file, second_file, file_format = get_parser()
    print(generate_diff(first_file, second_file, file_format))


if __name__ == '__main__':
    main()
