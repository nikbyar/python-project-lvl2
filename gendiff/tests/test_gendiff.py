
from gendiff.processor import process_to_python_format
from gendiff.parser import parse_files
from gendiff.tests.fixtures.test_string import STRING, STRING_NESTED
import pytest


TEST1_JSON1 = 'gendiff/tests/fixtures/test1_1.json'
TEST1_JSON2 = 'gendiff/tests/fixtures/test1_2.json'
TEST2_YML1 = 'gendiff/tests/fixtures/test2_1.yml'
TEST2_YML2 = 'gendiff/tests/fixtures/test2_2.yml'
TEST3_NESTED_JSON1 = 'gendiff/tests/fixtures/test3_nested1.json'
TEST3_NESTED_JSON2 = 'gendiff/tests/fixtures/test3_nested2.json'
TEST4_NESTED_YML1 = 'gendiff/tests/fixtures/test4_nested1.yml'
TEST4_NESTED_YML2 = 'gendiff/tests/fixtures/test4_nested2.yml'


@pytest.mark.parametrize(
    "input1, input2", [(TEST1_JSON1, TEST1_JSON2), (TEST2_YML1, TEST2_YML2)]
)
def test_generate_diff(input1, input2):
    file1, file2 = process_to_python_format(input1, input2)
    assert parse_files(file1, file2) == STRING


@pytest.mark.parametrize(
    "input_nested1, input_nested2", 
    [(TEST3_NESTED_JSON1, TEST3_NESTED_JSON2),
    (TEST4_NESTED_YML1, TEST4_NESTED_YML2)]
)
def test_generate_diff_nested(input_nested1, input_nested2):
    file1, file2 = process_to_python_format(input_nested1, input_nested2)
    assert parse_files(file1, file2) == STRING_NESTED