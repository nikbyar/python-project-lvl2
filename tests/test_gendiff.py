import pytest
from tests.fixtures.diff_string import diff_string, diff_string_stylish_nested, diff_string_plain
from gendiff.scripts.gendiff import generate_diff_, generate_diff_nested, build_diff_tree, stylish, plain


@pytest.fixture
def file1_json():
    return 'tests/fixtures/fixture_file1.json'


@pytest.fixture
def file2_json():
    return 'tests/fixtures/fixture_file2.json'


def test_generate_diff_json(file1_json, file2_json):
    result = stylish(file1_json, file2_json)
    assert result == diff_string


@pytest.fixture
def file1_yaml():
    return 'tests/fixtures/fixture_file1.yaml'


@pytest.fixture
def file2_yaml():
    return 'tests/fixtures/fixture_file2.yaml'


def test_generate_diff_yaml(file1_yaml, file2_yaml):
    result = stylish(file1_yaml, file2_yaml)
    assert result == diff_string


@pytest.fixture
def file1_json_nested():
    return 'tests/fixtures/fixture_file1_nested.json'


@pytest.fixture
def file2_json_nested():
    return 'tests/fixtures/fixture_file2_nested.json'


def test_generate_diff_json_nested(file1_json_nested, file2_json_nested):
    result = stylish(file1_json_nested, file2_json_nested)
    assert result == diff_string_stylish_nested


@pytest.fixture
def file1_yaml_nested():
    return 'tests/fixtures/fixture_file1_nested.yaml'


@pytest.fixture
def file2_yaml_nested():
    return 'tests/fixtures/fixture_file2_nested.yaml'


def test_generate_diff_yaml_nested(file1_yaml_nested, file2_yaml_nested):
    result = stylish(file1_yaml_nested, file2_yaml_nested)
    assert result == diff_string_stylish_nested


def test_generate_diff_plain_json(file1_json_nested, file2_json_nested):
    result = plain(file1_json_nested, file2_json_nested)
    assert result == diff_string_plain


def test_generate_diff_plain_yaml(file1_yaml_nested, file2_yaml_nested):
    result = plain(file1_yaml_nested, file2_yaml_nested)
    assert result == diff_string_plain