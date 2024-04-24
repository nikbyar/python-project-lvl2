# def build_diff_plain(pre_diff): # noqa: max-complexity=15
#     def walk(value, diff, path):
#         diff = ""
#         if isinstance(value, dict):
#             for key in value.keys():
#                 if not isinstance(value[key], list):
#                     if isinstance(value[key], dict):
#                         walk(value[key], diff, path + key + '.')
#                 elif value[key][0] == 'nested':
#                     diff += walk(value[key][1], diff, path + key + '.')
#                 elif value[key][0] == 'changed':
#                     prev_value = f"{value[key][1]}"
#                     new_value = f"{value[key][2]}"
#                     if isinstance(value[key][1], str):
#                         prev_value = f"'{value[key][1]}'"
#                     if isinstance(value[key][2], str):
#                         new_value = f"'{value[key][2]}'"
#                     if isinstance(value[key][1], dict):
#                         prev_value = '[complex value]'
#                     if isinstance(value[key][2], dict):
#                         new_value = '[complex value]'
#                     diff += f"Property '{path}{key}' was updated. " \
#                             f"From {prev_value} to {new_value}\n"
#                 elif value[key][0] == 'added' \
#                         and isinstance(value[key][1], dict):
#                     diff += f"Property '{path}{key}' was " \
#                             f"added with value: [complex value]\n"
#                 elif value[key][0] == 'added' \
#                         and not isinstance(value[key][1], dict):
#                     new_value = f"{value[key][1]}"
#                     if isinstance(value[key][1], str):
#                         new_value = f"'{value[key][1]}'"
#                     diff += f"Property '{path}{key}' was " \
#                             f"added with value: {new_value}\n"
#                 elif value[key][0] == 'deleted':
#                     diff += f"Property '{path}{key}' was removed\n"
#         if not isinstance(value, dict):
#             return str(value)
#         return diff
#     return '\n' + walk(pre_diff, '', '')

def build_diff_plain(pre_diff): # noqa: max-complexity=9
    def walk(value, diff, path):
        diff = ""
        if isinstance(value, dict):
            for node in value.keys():
                if not isinstance(value[node], list):
                    transform_dict_node(walk(), value[node], diff, path, node)

                elif value[node][0] == 'nested':
                    diff += walk(value[node][1], diff, path + node + '.')

                elif value[node][0] == 'changed':
                    diff += transform_changed_node(node, value[node][1],
                                                   value[node][2], path)

                elif value[node][0] == 'added':
                    diff += transform_added_node(node, value[node][1], path)

                elif value[node][0] == 'deleted':
                    diff += transform_deleted_node(node, path)
        else:
            return str(value)
        return diff
    return '\n' + walk(pre_diff, '', '')


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


def transform_dict_node(func, value_node, diff, path, node):
    if isinstance(value_node, dict):
        func(value_node, diff, path + node + '.')


def replace_bools_in_plain(diff):
    return diff.replace("False", 'false').replace("None", "null").\
        replace("True", "true").strip()


def make_plain(pre_diff):
    return replace_bools_in_plain(build_diff_plain(pre_diff))
