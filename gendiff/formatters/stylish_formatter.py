import json


SPACES = '    '
SPACES_PLUS = '  + '
SPACES_MINUS = '  - '


def make_stylish(pre_diff):
    return '{' + walk(pre_diff, 1) + '\n}'


def walk(diff, depth): # noqa: max-complexity=7
    result = ''
    for node, value_node in diff.items():
        if value_node[0] == 'nested':
            result += transform_nested_node(node, value_node[1], depth)
        elif value_node[0] == 'changed':
            result += transform_changed_node(node, value_node[1],
                                             value_node[2], depth)
        elif value_node[0] == 'added':
            result += transform_added_node(node, value_node[1], depth)
        elif value_node[0] == 'deleted':
            result += transform_deleted_node(node, value_node[1], depth)
        elif value_node[0] == 'unchanged':
            result += transform_unchanged_node(node, value_node[1], depth)
    return result


def transform_value(value, depth):
    if isinstance(value, dict):
        result = '{'
        for key, val in value.items():
            if isinstance(val, list):
                return '{' + walk(value, depth) + f'\n{SPACES * (depth - 1)}}}'

            result += f'\n{SPACES * depth}{key}: ' \
                      f'{transform_value(val, depth + 1)}'
        result += f'\n{SPACES * (depth - 1)}}}'
        return result

    else:
        return transform_bool(value)


def transform_unchanged_node(node, value_node, depth):
    return f'\n{SPACES * depth}{node}: {transform_bool(value_node)}'


def transform_nested_node(node, value_node, depth):
    result = f'\n{SPACES * depth}{node}: '
    result += transform_value(value_node, depth + 1)
    return result


def transform_changed_node(node, value_node1, value_node2, depth):
    result = f'\n{SPACES * (depth - 1) + SPACES_MINUS}{node}: '
    result += transform_value(value_node1, depth + 1)
    result += f'\n{SPACES * (depth - 1) + SPACES_PLUS}{node}: '
    result += transform_value(value_node2, depth + 1)
    return result


def transform_added_node(node, value_node, depth):
    if isinstance(value_node, dict):
        result = f'\n{SPACES * (depth - 1) + SPACES_PLUS}{node}: '
        result += transform_value(value_node, depth + 1)
        return result
    else:
        return f'\n{SPACES * (depth - 1) + SPACES_PLUS}{node}: ' \
               f'{transform_bool(value_node)}'


def transform_deleted_node(node, value_node, depth):
    if isinstance(value_node, dict):
        result = f'\n{SPACES * (depth - 1) + SPACES_MINUS}{node}: '
        result += transform_value(value_node, depth + 1)
        return result
    else:
        return f'\n{SPACES * (depth - 1) + SPACES_MINUS}{node}: ' \
               f'{transform_bool(value_node)}'


def transform_bool(value):
    if value in (True, False, None):
        return json.dumps(value)
    return str(value)
