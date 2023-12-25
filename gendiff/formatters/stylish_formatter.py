def build_diff_stylish(pre_diff): # noqa: max-complexity=15
    SPACES = '    '
    SPACES_PLUS = '  + '
    SPACES_MINUS = '  - '

    def walk(value, diff, depth):
        if isinstance(value, dict):
            diff = '{'
            for key in value.keys():
                if not isinstance(value[key], list):
                    if isinstance(value[key], dict):
                        diff += f'\n{SPACES * depth}{key}: '
                        diff += walk(value[key], diff, depth + 1)
                    elif not isinstance(value[key], dict):
                        diff += f'\n{SPACES * depth}{key}: {value[key]}'

                elif value[key][0] == 'changed' and len(value[key]) == 2:
                    diff += f'\n{SPACES * depth}{key}: '
                    diff += walk(value[key][1], diff, depth + 1)
                elif value[key][0] == 'changed' and len(value[key]) == 3:
                    diff += f'\n{SPACES * (depth - 1) + SPACES_MINUS}{key}: '
                    diff += walk(value[key][1], diff, depth + 1)
                    diff += f'\n{SPACES * (depth - 1) + SPACES_PLUS}{key}: '
                    diff += walk(value[key][2], diff, depth + 1)
                elif value[key][0] == 'added' \
                        and isinstance(value[key][1], dict):
                    diff += f'\n{SPACES * (depth - 1) + SPACES_PLUS}{key}: '
                    diff += walk(value[key][1], diff, depth + 1)
                elif value[key][0] == 'added' \
                        and not isinstance(value[key][1], dict):
                    diff += f'\n{SPACES * (depth - 1) + SPACES_PLUS}{key}: ' \
                            f'{value[key][1]}'
                elif value[key][0] == 'deleted' \
                        and isinstance(value[key][1], dict):
                    diff += f'\n{SPACES * (depth - 1) + SPACES_MINUS}{key}: '
                    diff += walk(value[key][1], diff, depth + 1)
                elif value[key][0] == 'deleted' \
                        and not isinstance(value[key][1], dict):
                    diff += f'\n{SPACES * (depth - 1) + SPACES_MINUS}{key}: ' \
                            f'{value[key][1]}'
                elif value[key][0] == 'unchanged':
                    diff += f'\n{SPACES * depth}{key}: {value[key][1]}'
        if not isinstance(value, dict):
            return str(value)
        diff += f'\n{SPACES * (depth - 1)}}}'
        return diff
    return walk(pre_diff, ' ', 1)


def replace_bools_in_stylish(diff):
    return diff.replace('False', 'false').replace('None', 'null').\
        replace('True', 'true')


def make_stylish(pre_diff):
    return replace_bools_in_stylish(build_diff_stylish(pre_diff))
