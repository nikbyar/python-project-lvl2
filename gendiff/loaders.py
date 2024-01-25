import json
import yaml


def load_json(file):
    try:
        return json.load(open(file))
    except FileNotFoundError:
        return json.loads(file)


def load_yaml(file):
    try:
        return yaml.safe_load(open(file))
    except FileNotFoundError:
        return yaml.safe_load(file)
