
from gendiff.gendiff import generate_diff
from gendiff.tests.fixtures.test_string import STRING


def test_generate_diff():
    test1 = 'gendiff/tests/fixtures/test1.json'
    test2 = 'gendiff/tests/fixtures/test2.json'
    assert generate_diff(test1, test2) == STRING
