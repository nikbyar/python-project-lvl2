
from gendiff.processor import process_to_python_format
from gendiff.parser import parse_files
from gendiff.tests.fixtures.test_string import STRING
import pytest


TEST1_JSON = 'gendiff/tests/fixtures/test1.json'
TEST2_JSON = 'gendiff/tests/fixtures/test2.json'
TEST1_YML = 'gendiff/tests/fixtures/test1.yml'
TEST2_YML = 'gendiff/tests/fixtures/test2.yml'


@pytest.mark.parametrize(
    "input1, input2", [(TEST1_JSON, TEST2_JSON), (TEST1_YML, TEST2_YML)]
)
def test_generate_diff(input1, input2):
    file1, file2 = process_to_python_format(input1, input2)
    assert parse_files(file1, file2) == STRING
