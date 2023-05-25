import pytest
from tests.fixtures.diff_string import diff_string_json, diff_string_yaml
from gendiff.scripts.gendiff import generate_diff


@pytest.fixture
def first_file_json():
    return 'tests/fixtures/fixture_file1.json'


@pytest.fixture
def second_file_json():
    return 'tests/fixtures/fixture_file2.json'


def test_generate_diff_json(first_file_json, second_file_json):
    result = generate_diff(first_file_json, second_file_json)
    assert result == diff_string_json


@pytest.fixture
def first_file_yaml():
    return 'tests/fixtures/fixture_file1.yaml'


@pytest.fixture
def second_file_yaml():
    return 'tests/fixtures/fixture_file2.yaml'


def test_generate_diff_yaml(first_file_yaml, second_file_yaml):
    result = generate_diff(first_file_yaml, second_file_yaml)
    assert result == diff_string_yaml
