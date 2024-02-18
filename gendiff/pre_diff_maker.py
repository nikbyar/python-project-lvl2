def generate_pre_diff(dict1, dict2):  # noqa: max-complexity=15
    diff = {}

    def inner(dict1, dict2, merged_dict):
        all_keys = dict1.keys() | dict2.keys()

        for key in sorted(all_keys):
            if key not in dict1.keys():
                merged_dict[key] = ['added', dict2.get(key)]
            elif key not in dict2.keys():
                merged_dict[key] = ['deleted', dict1.get(key)]
            elif dict1[key] == dict2[key]:
                merged_dict[key] = ['unchanged', dict1.get(key)]
            elif isinstance(dict1.get(key), dict) and \
                    isinstance(dict2.get(key), dict):
                merged_dict[key] = ['changed', {}]
                inner(dict1.get(key), dict2.get(key), merged_dict[key][1])
            else:
                merged_dict[key] = ['changed', dict1.get(key), dict2.get(key)]

    inner(dict1, dict2, diff)
    return diff
