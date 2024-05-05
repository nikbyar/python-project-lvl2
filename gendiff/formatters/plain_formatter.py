def build_diff_plain(pre_diff): # noqa: max-complexity=9
    return walk(pre_diff, '')

#
# def transform_value(value):
#     if isinstance(value, dict):
#         return 222
#         # return '{' + ', '.join([f"'{key}': {transform_value(val)}" for key, val in value.items()]) + '}'
#     else:
#         return str(value)


def walk(value, path):
    diff = ''
    # if isinstance(value, dict):
    for node, val in value.items():
        if not isinstance(val, list):
            diff += transform_dict_node(val, path, node)
        elif val[0] == 'nested':
            diff += walk(val[1], f'{path}{node}.')
        elif val[0] == 'changed':
            diff += transform_changed_node(node, val[1], val[2], path)
        elif val[0] == 'added':
            diff += transform_added_node(node, val[1], path)
        elif val[0] == 'deleted':
            diff += transform_deleted_node(node, path)
    # else:
    #     return str.upper(value)
    return diff




def transform_dict_node(value, path, node):
    return f"Property '{path}{node}' was updated. From {value[1]} to {value[2]}.\n"


def transform_deleted_node(node, path):
    return f"Property '{path}{node}' was removed\n"


def transform_added_node(node, node_value, path):
    if isinstance(node_value, dict):
        return f"Property '{path}{node}' was " \
               f"added with value: [complex value]\n"

    new_value = f"{node_value}"
    if isinstance(node_value, str):
        new_value = f"'{node_value}'"
    return f"Property '{path}{node}' was " \
           f"added with value: {new_value}\n"


def transform_changed_node(node, prev_value_, new_value_, path):
    prev_value = f"{prev_value_}"
    new_value = f"{new_value_}"
    if isinstance(prev_value_, str):
        prev_value = f"'{prev_value_}'"
    if isinstance(new_value_, str):
        new_value = f"'{new_value_}'"
    if isinstance(prev_value_, dict):
        prev_value = '[complex value]'
    if isinstance(new_value_, dict):
        new_value = '[complex value]'
    return f"Property '{path}{node}' was updated. "\
           f"From {prev_value} to {new_value}\n"


def replace_bools_in_plain(diff):
    return diff.replace("False", 'false').replace("None", "null").\
        replace("True", "true").strip()


def make_plain(pre_diff):
    return replace_bools_in_plain(build_diff_plain(pre_diff))
