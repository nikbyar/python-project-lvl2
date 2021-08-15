TWO_SPACES = "  "
FOUR_SPACES = "    "


def parse_files(file1, file2):
    keys = file1.keys() | file2.keys()
    diff_string = []
    for key in sorted(keys):
        if key in file1 and key in file2:
            if file1[key] == file2[key]:
                diff_string.append(f'{FOUR_SPACES}{key}: {file1[key]} \n')
            else:
                diff_string.append(f'{TWO_SPACES}- {key}: {file1[key]} \n')
                diff_string.append(f'{TWO_SPACES}+ {key}: {file2[key]} \n')
        elif key in file1:
            diff_string.append(f'{TWO_SPACES}- {key}: {file1[key]} \n')
        elif key in file2:
            diff_string.append(f'{TWO_SPACES}+ {key}: {file2[key]} \n')
    diff_string = '{{\n{}}}'.format(''.join(diff_string))
    return ''.join(diff_string)
