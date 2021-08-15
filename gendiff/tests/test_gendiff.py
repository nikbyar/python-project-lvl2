
from gendiff.gendiff_json import generate_diff_json
from gendiff.gendiff_yml import generate_diff_yml
from gendiff.parser import parse_files
from gendiff.tests.fixtures.test_string import STRING


def test_generate_diff_json():
    test1 = 'gendiff/tests/fixtures/test1.json'
    test2 = 'gendiff/tests/fixtures/test2.json'
    file1, file2 = generate_diff_json(test1, test2)
    assert parse_files(file1, file2) == STRING


def test_generate_diff_yml():
    test1 = 'gendiff/tests/fixtures/test1.yml'
    test2 = 'gendiff/tests/fixtures/test2.yml'
    file1, file2 = generate_diff_yml(test1, test2)
    assert parse_files(file1, file2) == STRING
