import json
import yaml


def determine_format_if_file(file):
    if file.lower().endswith('json'):
        return 'json'
    elif file.lower().endswith(('yaml', 'yml')):
        return 'yaml'


def determine_format(file):
    try:
        response = file
        response.json()
        return 'json'
    except AttributeError:
        return determine_format_if_file(file)
    except json.JSONDecodeError:
        pass

    try:
        yaml.safe_load(response.text)
        return 'yaml'
    except yaml.YAMLError:
        return 'Unknown format'
