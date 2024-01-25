import pytest
import json


from gendiff.gendiff import generate_diff


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


file1_json = 'tests/fixtures/fixture_file1.json'
file2_json = 'tests/fixtures/fixture_file2.json'
file1_yaml = 'tests/fixtures/fixture_file1.yaml'
file2_yaml = 'tests/fixtures/fixture_file2.yaml'
file1_json_nested = 'tests/fixtures/fixture_file1_nested.json'
file2_json_nested = 'tests/fixtures/fixture_file2_nested.json'
file1_yaml_nested = 'tests/fixtures/fixture_file1_nested.yaml'
file2_yaml_nested = 'tests/fixtures/fixture_file2_nested.yaml'


@pytest.mark.parametrize("file1, file2, result", [
    (file1_json, file2_json, diff_string),
    (file1_yaml, file2_yaml, diff_string),
    (file1_json_nested, file2_json_nested, diff_string_stylish),
    (file1_yaml_nested, file2_yaml_nested, diff_string_stylish)
])
def test_generate_diff(file1, file2, result):
    assert generate_diff(file1, file2) == result


@pytest.mark.parametrize("file1, file2, format, result", [
    (file1_json_nested, file2_json_nested, 'stylish', diff_string_stylish),
    (file1_yaml_nested, file2_yaml_nested, 'stylish', diff_string_stylish),
    (file1_json_nested, file2_json_nested, 'plain', diff_string_plain),
    (file1_yaml_nested, file2_yaml_nested, 'plain', diff_string_plain),
    (file1_json_nested, file2_json_nested, 'json', diff_string_json),
    (file1_yaml_nested, file2_yaml_nested, 'json', diff_string_json),
])
def test_generate_diff_with_format(file1, file2, format, result):
    assert generate_diff(file1, file2, format) == result
