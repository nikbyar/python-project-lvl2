from gendiff.parser import TWO_SPACES as TS, FOUR_SPACES as FS
STRING = (
    '{{\n{0}- test_key: string \n{0}+ test_key: long_string \n'
    '{1}test_key_a: 2 \n{0}+ test_key_b: False \n}}'.format(TS, FS)
)
