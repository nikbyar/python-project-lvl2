import pytest
from tests.fixtures.diff_string import diff_string
from gendiff.scripts.gendiff import generate_diff


@pytest.fixture
def first_file():
    return 'tests/fixtures/fixture_file1.json'


@pytest.fixture
def second_file():
    return 'tests/fixtures/fixture_file2.json'


def test_generate_diff(first_file, second_file):
    result = generate_diff(first_file, second_file)
    assert result == diff_string
