def generate_pre_diff(dict1, dict2, diff={}):

    all_keys = dict1.keys() | dict2.keys()

    for key in sorted(all_keys):
        if key not in dict1.keys():
            diff[key] = ['added', dict2.get(key)]
        elif key not in dict2.keys():
            diff[key] = ['deleted', dict1.get(key)]
        elif dict1[key] == dict2[key]:
            diff[key] = ['unchanged', dict1.get(key)]
        elif isinstance(dict1.get(key), dict) and \
                isinstance(dict2.get(key), dict):
            diff[key] = ['nested', {}]
            generate_pre_diff(dict1.get(key), dict2.get(key), diff[key][1])
        else:
            diff[key] = ['changed', dict1.get(key), dict2.get(key)]

    return diff
