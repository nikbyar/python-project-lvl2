import json


TWO_SPACES = "  "
FOUR_SPACES = "    "


def generate_diff(file_path1, file_path2):
    # file1 = json.load(open('gendiff/scripts/file1.json'))
    # file2 = json.load(open('gendiff/scripts/file2.json'))
    file1 = json.load(open(file_path1))
    file2 = json.load(open(file_path2))
    keys = file1.keys() | file2.keys()
    a = []
    for key in sorted(keys):
        if key in file1 and key in file2:
            if file1[key] == file2[key]:
                a.append('{0}{1}: {2} \n'.format(FOUR_SPACES, key, file1[key]))
            else:
                a.append('{0}- {1}: {2} \n'.format(TWO_SPACES, key, file1[key]))
                a.append('{0}+ {1}: {2} \n'.format(TWO_SPACES, key, file2[key]))
        elif key in file1:
            a.append('{0}- {1}: {2} \n'.format(TWO_SPACES, key, file1[key]))
        elif key in file2:
            a.append('{0}+ {1}: {2} \n'.format(TWO_SPACES, key, file2[key]))
    a = '{{\n{}}}'.format(''.join(a))
    print(''.join(a))
