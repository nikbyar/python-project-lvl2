from gendiff.parser import TWO_SPACES as TS, FOUR_SPACES as FS
STRING = (
    '{{\n{0}- follow: False \n{1}host: hexlet.io \n'
    '{0}- proxy: 123.234.53.22 \n{0}- timeout: 50 \n'
    '{0}+ timeout: 20 \n{0}+ verbose: True \n}}'.format(TS, FS)
)

STRING_NESTED = (
    '{{\n{1}common: {{\n{0}{1}+ follow: false\n{1}{1}setting1: Value 1\n'
    '{0}{1}- setting2: 200\n{0}{1}- setting3: true\n{0}{1}+ setting3: null\n'
    '{0}{1}+ setting4: blah blah\n{0}{1}+ setting5: {{\n'
    '{1}{1}{1}key5: value5\n{1}{1}}}\n{1}{1}setting6: {{\n{1}{1}{1}doge: {{\n'
    '{1}{1}{1}{0}- wow:\n{1}{1}{1}{0}+ wow: so much\n{1}{1}{1}}}\n'
    '{1}{1}{1}key: value\n{1}{1}{0}+ ops: vops\n{1}{1}}}\n{1}}}\n'
    '{1}group1: {{\n{1}{0}- baz: bas\n{1}{0}+ baz: bars\n{1}{1}foo: bar\n'
    '{1}{0}- nest: {{\n{1}{1}{1}key: value\n{1}{1}}}\n{1}{0}+ nest: str\n'
    '{1}}}\n{0}- group2: {{\n{1}{1}abc: 12345\n{1}{1}deep: {{\n'
    '{1}{1}{1}id: 45\n{1}{1}}}\n{1}}}\n{0}+ group3: {{\n{1}{1}deep: {{\n'
    '{1}{1}{1}id: {{\n{1}{1}{1}{1}number: 45\n{1}{1}{1}}}\n{1}{1}}}\n'
    '{1}{1}fee: 100500\n{1}}}\n}}'.format(TS, FS)
)
