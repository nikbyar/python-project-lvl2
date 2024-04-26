def build_diff_stylish(pre_diff): # noqa: max-complexity=15
    SPACES = '    '
    SPACES_PLUS = '  + '
    SPACES_MINUS = '  - '

    def walk(value, diff, depth):
        if isinstance(value, dict):
            diff = '{'
            for node in value.keys():
                if not isinstance(value[node], list):
                    diff += transform_dict_node(walk, diff, node, value[node],
                                                depth, SPACES)

                elif value[node][0] == 'nested':
                    diff += transform_nested_node(walk, diff, node,
                                                  value[node][1], depth, SPACES)

                elif value[node][0] == 'changed':
                    diff += transform_changed_node(
                        walk, diff, node, value[node][1], value[node][2],
                        depth, SPACES, SPACES_PLUS, SPACES_MINUS)

                elif value[node][0] == 'added':
                    diff += transform_added_node(
                        walk, diff, node, value[node][1], depth,
                        SPACES, SPACES_PLUS)

                elif value[node][0] == 'deleted':
                    diff += transform_deleted_node(
                        walk, diff, node, value[node][1], depth,
                        SPACES, SPACES_MINUS)

                elif value[node][0] == 'unchanged':
                    diff += transform_unchanged_node(node, value[node][1],
                                                     depth, SPACES)
        if not isinstance(value, dict):
            return str(value)
        diff += f'\n{SPACES * (depth - 1)}}}'
        return diff
    return walk(pre_diff, ' ', 1)


def transform_dict_node(func, diff, node, value_node, depth,
                        SPACES):
    if isinstance(value_node, dict):
        result = f'\n{SPACES * depth}{node}: '
        result += func(value_node, diff, depth + 1)
    else:
        result = f'\n{SPACES * depth}{node}: {value_node}'
    return result


def transform_nested_node(func, diff, node, value_node, depth,
                          SPACES):
    result = f'\n{SPACES * depth}{node}: '
    result += func(value_node, diff, depth + 1)
    return result


def transform_changed_node(func, diff, node, value_node1, value_node2, depth,
                           SPACES, SPACES_PLUS, SPACES_MINUS):
    result = f'\n{SPACES * (depth - 1) + SPACES_MINUS}{node}: '
    result += func(value_node1, diff, depth + 1)
    result += f'\n{SPACES * (depth - 1) + SPACES_PLUS}{node}: '
    result += func(value_node2, diff, depth + 1)
    return result


def transform_added_node(func, diff, node, value_node, depth,
                         SPACES, SPACES_PLUS):
    if isinstance(value_node, dict):
        result = f'\n{SPACES * (depth - 1) + SPACES_PLUS}{node}: '
        result += func(value_node, diff, depth + 1)
        return result

    else:
        return f'\n{SPACES * (depth - 1) + SPACES_PLUS}{node}: '\
               f'{value_node}'


def transform_deleted_node(func, diff, node, value_node, depth,
                           SPACES, SPACES_MINUS):
    if isinstance(value_node, dict):
        result = f'\n{SPACES * (depth - 1) + SPACES_MINUS}{node}: '
        result += func(value_node, diff, depth + 1)
        return result
    else:
        return f'\n{SPACES * (depth - 1) + SPACES_MINUS}{node}: '\
               f'{value_node}'


def transform_unchanged_node(node, value_node, depth, SPACES):
    return f'\n{SPACES * depth}{node}: {value_node}'


def replace_bools_in_stylish(diff):
    return diff.replace('False', 'false').replace('None', 'null').\
        replace('True', 'true')


def make_stylish(pre_diff):
    return replace_bools_in_stylish(build_diff_stylish(pre_diff))
