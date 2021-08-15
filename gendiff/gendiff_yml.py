import yaml


def generate_diff_yml(file_path1, file_path2):
    file1 = yaml.full_load(open(file_path1))
    file2 = yaml.full_load(open(file_path2))
    return file1, file2

# print(generate_diff_yml('gendiff/file1.yml', 'gendiff/file2.yml'))
