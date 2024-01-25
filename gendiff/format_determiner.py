import json
import yaml


def determine_format(file):
    try:
        json.loads(file)
        return 'json'
    except ValueError:
        try:
            yaml.safe_load(file)
            return 'yaml'
        except yaml.YAMLError:
            return 'Unknown format'
