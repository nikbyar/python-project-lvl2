from gendiff.formatters.stylish_formatter import transform_bool


def make_plain(pre_diff):
    return walk(pre_diff, '').strip()


def walk(value, path): # noqa: max-complexity=7
    diff = ''
    for node, val in value.items():
        if val[0] == 'nested':
            diff += walk(val[1], f'{path}{node}.')
        elif val[0] == 'changed':
            diff += transform_changed_node(node, val[1], val[2], path)
        elif val[0] == 'added':
            diff += transform_added_node(node, val[1], path)
        elif val[0] == 'deleted':
            diff += transform_deleted_node(node, path)
    return diff


def transform_deleted_node(node, path):
    return f"Property '{path}{node}' was removed\n"


def transform_added_node(node, node_value, path):
    if isinstance(node_value, dict):
        return f"Property '{path}{node}' was " \
               f"added with value: [complex value]\n"

    new_value = f"{transform_bool(node_value)}"
    if isinstance(node_value, str):
        new_value = f"'{node_value}'"
    return f"Property '{path}{node}' was " \
           f"added with value: {new_value}\n"


def transform_changed_node(node, prev_value_, new_value_, path):
    prev_value = f"{transform_bool(prev_value_)}"
    new_value = f"{transform_bool(new_value_)}"
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
