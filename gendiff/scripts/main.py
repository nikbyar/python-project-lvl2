from gendiff.parser import parse_args
from gendiff.gendiff import generate_diff


def main():
    first_file, second_file, file_format = parse_args()
    print(generate_diff(first_file, second_file, file_format))


if __name__ == '__main__':
    main()
