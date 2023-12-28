import pytest
import json


from gendiff.scripts.gendiff import generate_diff


with open('tests/fixtures/diff_string', 'r') as f:
    diff_string = f.read()


with open('tests/fixtures/diff_string_stylish', 'r') as f:
    diff_string_stylish = ''
    for line in f:
        if '- wow:' in line:
            diff_string_stylish += line.rstrip() + ' ' + '\n'
        else:
            diff_string_stylish += line
    diff_string_stylish = diff_string_stylish.rstrip()


with open('tests/fixtures/diff_string_plain', 'r') as f:
    diff_string_plain = f.read()


diff_string_json = json.dumps(diff_string_stylish)


@pytest.fixture
def file1_json():
    return 'tests/fixtures/fixture_file1.json'


@pytest.fixture
def file2_json():
    return 'tests/fixtures/fixture_file2.json'


def test_generate_diff_json(file1_json, file2_json):
    result = generate_diff(file1_json, file2_json)
    assert result == diff_string


@pytest.fixture
def file1_yaml():
    return 'tests/fixtures/fixture_file1.yaml'


@pytest.fixture
def file2_yaml():
    return 'tests/fixtures/fixture_file2.yaml'


def test_generate_diff_yaml(file1_yaml, file2_yaml):
    result = generate_diff(file1_yaml, file2_yaml)
    assert result == diff_string


@pytest.fixture
def file1_json_nested():
    return 'tests/fixtures/fixture_file1_nested.json'


@pytest.fixture
def file2_json_nested():
    return 'tests/fixtures/fixture_file2_nested.json'


def test_generate_diff_json_stylish(file1_json_nested, file2_json_nested):
    result = generate_diff(file1_json_nested, file2_json_nested)
    assert result == diff_string_stylish


@pytest.fixture
def file1_yaml_nested():
    return 'tests/fixtures/fixture_file1_nested.yaml'


@pytest.fixture
def file2_yaml_nested():
    return 'tests/fixtures/fixture_file2_nested.yaml'


def test_generate_diff_yaml_stylish(file1_yaml_nested, file2_yaml_nested):
    result = generate_diff(file1_yaml_nested, file2_yaml_nested)
    assert result == diff_string_stylish


def test_generate_diff_json_plain(file1_json_nested, file2_json_nested):
    result = generate_diff(file1_json_nested, file2_json_nested, 'plain')
    assert result == diff_string_plain


def test_generate_diff_yaml_plain(file1_yaml_nested, file2_yaml_nested):
    result = generate_diff(file1_yaml_nested, file2_yaml_nested, 'plain')
    assert result == diff_string_plain


def test_generate_diff_json_output(file1_json_nested, file2_yaml_nested):
    result = generate_diff(file1_json_nested, file2_yaml_nested, 'json')
    assert result == diff_string_json
