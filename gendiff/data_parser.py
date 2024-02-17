from gendiff.loaders import load_json_from_file, load_yaml_from_file, \
    load_json_from_network, load_yaml_from_network


def parse(data, format):

    loaders = {
        'json': (load_json_from_network, load_json_from_file),
        'yaml': (load_yaml_from_network, load_yaml_from_file)
    }
    load_from_network, load_from_file = loaders.get(format)

    try:
        return load_from_file(data)
    except TypeError:
        return load_from_network(data)
