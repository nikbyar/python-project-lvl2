import json
import yaml


def load_json_from_file(file):
    return json.load(open(file))


def load_json_from_network(file):
    return json.loads(file.text)


def load_yaml_from_file(file):
    return yaml.safe_load(open(file))


def load_yaml_from_network(file):
    return yaml.safe_load(file.text)
