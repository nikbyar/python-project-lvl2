from gendiff.parser import TWO_SPACES as TS, FOUR_SPACES as FS
STRING = (
    '{{\n{0}- follow: False \n{1}host: hexlet.io \n'
    '{0}- proxy: 123.234.53.22 \n{0}- timeout: 50 \n'
    '{0}+ timeout: 20 \n{0}+ verbose: True \n}}'.format(TS, FS)
)
