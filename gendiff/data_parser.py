from gendiff.loaders import load_json, load_yaml


def parse(data, format):
    if format == 'json':
        return load_json(data)
    elif format == 'yaml':
        return load_yaml(data)
