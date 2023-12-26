def build_diff_plain(pre_diff): # noqa: max-complexity=15
    def walk(value, diff, path):
        diff = ""
        if isinstance(value, dict):
            for key in value.keys():
                if not isinstance(value[key], list):
                    if isinstance(value[key], dict):
                        walk(value[key], diff, path + key + '.')
                elif value[key][0] == 'changed' and len(value[key]) == 2:
                    diff += walk(value[key][1], diff, path + key + '.')
                elif value[key][0] == 'changed' and len(value[key]) == 3:
                    prev_value = f"{value[key][1]}"
                    new_value = f"{value[key][2]}"
                    if isinstance(value[key][1], str):
                        prev_value = f"'{value[key][1]}'"
                    if isinstance(value[key][2], str):
                        new_value = f"'{value[key][2]}'"
                    if isinstance(value[key][1], dict):
                        prev_value = '[complex value]'
                    if isinstance(value[key][2], dict):
                        new_value = '[complex value]'
                    diff += f"Property '{path}{key}' was updated. " \
                            f"From {prev_value} to {new_value}\n"
                elif value[key][0] == 'added' \
                        and isinstance(value[key][1], dict):
                    diff += f"Property '{path}{key}' was " \
                            f"added with value: [complex value]\n"
                elif value[key][0] == 'added' \
                        and not isinstance(value[key][1], dict):
                    new_value = f"{value[key][1]}"
                    if isinstance(value[key][1], str):
                        new_value = f"'{value[key][1]}'"
                    diff += f"Property '{path}{key}' was " \
                            f"added with value: {new_value}\n"
                elif value[key][0] == 'deleted':
                    diff += f"Property '{path}{key}' was removed\n"
        if not isinstance(value, dict):
            return str(value)
        return diff
    return '\n' + walk(pre_diff, '', '')


def replace_bools_in_plain(diff):
    return diff.replace("False", 'false').replace("None", "null").\
        replace("True", 'true').strip()


def make_plain(pre_diff):
    return replace_bools_in_plain(build_diff_plain(pre_diff))
