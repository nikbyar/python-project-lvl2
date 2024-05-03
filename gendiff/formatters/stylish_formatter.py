import json


SPACES = '    '
SPACES_PLUS = '  + '
SPACES_MINUS = '  - '


# def build_diff_stylish(pre_diff): # noqa: max-complexity=15
#
#     def walk(value, diff, depth):
#         if isinstance(value, dict):
#             diff = '{'
#             for node in value.keys():
#                 if not isinstance(value[node], list):
#                     diff += transform_dict_node(walk, diff, node, value[node],
#                                                 depth)
#
#                 elif value[node][0] == 'nested':
#                     diff += transform_nested_node(walk, diff, node,
#                                                   value[node][1], depth)
#
#                 elif value[node][0] == 'changed':
#                     diff += transform_changed_node(
#                         walk, diff, node, value[node][1], value[node][2],
#                         depth)
#
#                 elif value[node][0] == 'added':
#                     diff += transform_added_node(
#                         walk, diff, node, value[node][1], depth)
#
#                 elif value[node][0] == 'deleted':
#                     diff += transform_deleted_node(
#                         walk, diff, node, value[node][1], depth)
#
#                 elif value[node][0] == 'unchanged':
#                     diff += transform_unchanged_node(node, value[node][1],
#                                                      depth)
#         if not isinstance(value, dict):
#             return str(value)
#         diff += f'\n{SPACES * (depth - 1)}}}'
#         return diff
#     return walk(pre_diff, ' ', 1)
#
#
# def transform_dict_node(func, diff, node, value_node, depth):
#     if isinstance(value_node, dict):
#         result = f'\n{SPACES * depth}{node}: '
#         result += func(value_node, diff, depth + 1)
#     else:
#         result = f'\n{SPACES * depth}{node}: {value_node}'
#     return result
#
#
# def transform_nested_node(func, diff, node, value_node, depth):
#     result = f'\n{SPACES * depth}{node}: '
#     result += func(value_node, diff, depth + 1)
#     return result
#
#
# def transform_changed_node(func, diff, node, value_node1, value_node2, depth):
#     result = f'\n{SPACES * (depth - 1) + SPACES_MINUS}{node}: '
#     result += func(value_node1, diff, depth + 1)
#     result += f'\n{SPACES * (depth - 1) + SPACES_PLUS}{node}: '
#     result += func(value_node2, diff, depth + 1)
#     return result
#
#
# def transform_added_node(func, diff, node, value_node, depth):
#     if isinstance(value_node, dict):
#         result = f'\n{SPACES * (depth - 1) + SPACES_PLUS}{node}: '
#         result += func(value_node, diff, depth + 1)
#         return result
#
#     else:
#         return f'\n{SPACES * (depth - 1) + SPACES_PLUS}{node}: '\
#                f'{value_node}'
#
#
# def transform_deleted_node(func, diff, node, value_node, depth):
#     if isinstance(value_node, dict):
#         result = f'\n{SPACES * (depth - 1) + SPACES_MINUS}{node}: '
#         result += func(value_node, diff, depth + 1)
#         return result
#     else:
#         return f'\n{SPACES * (depth - 1) + SPACES_MINUS}{node}: '\
#                f'{value_node}'

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


def walk(diff, depth): # noqa: max-complexity=7
    result = ''
    for node, value_node in diff.items():
        # if not isinstance(value_node, list):
        #     result += transform_dict_node(node, value_node, depth)
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


def build_diff_stylish(pre_diff):
    return '{' + walk(pre_diff, 1) + '\n}'


def transform_unchanged_node(node, value_node, depth):
    return f'\n{SPACES * depth}{node}: {transform_bool(value_node)}'
#
# def transform_dict_node(node, value_node, depth):
#     if isinstance(value_node, dict):
#         result = f'\n{SPACES * depth}{node}: '
#         result += transform_value(value_node, depth + 1)
#     else:
#         result = f'\n{SPACES * depth}{node}: {value_node}'
#     return result


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

# def replace_bools_in_stylish(diff):
#     return diff.replace('False', 'false').replace('None', 'null').\
#         replace('True', 'true')


def make_stylish(pre_diff):
    # return replace_bools_in_stylish(build_diff_stylish(pre_diff))
    return build_diff_stylish(pre_diff)
