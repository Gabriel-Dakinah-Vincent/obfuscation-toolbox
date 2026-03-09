import pytest
from obfuscation_toolit import obfuscate, deobfuscate


def test_string_obfuscator():
    code = "print('hello world')"
    obfuscated = obfuscate('string', code, level=1)
    deobfuscated = deobfuscate('string', obfuscated, level=1)
    assert deobfuscated == code
    assert obfuscated != code


def test_hex_obfuscator():
    code = "x = 10"
    obfuscated = obfuscate('hex', code)
    deobfuscated = deobfuscate('hex', obfuscated)
    assert deobfuscated == code
    assert obfuscated != code


def test_variable_obfuscator():
    code = "x = 5\ny = 10\nprint(x + y)"
    obfuscated = obfuscate('variable', code, length=8)
    assert obfuscated != code
    assert 'x' not in obfuscated or 'y' not in obfuscated


def test_control_flow_obfuscator():
    code = "x = 1\nprint(x)"
    obfuscated = obfuscate('control_flow', code, complexity=2)
    deobfuscated = deobfuscate('control_flow', obfuscated, complexity=2)
    assert obfuscated != code
    assert len(obfuscated.split('\n')) > len(code.split('\n'))


def test_comment_obfuscator():
    code = "x = 5\ny = 10"
    obfuscated = obfuscate('comment', code, density=1)
    deobfuscated = deobfuscate('comment', obfuscated, density=1)
    assert obfuscated != code
    assert len(obfuscated.split('\n')) > len(code.split('\n'))


def test_invalid_method():
    with pytest.raises(ValueError):
        obfuscate('invalid_method', "code")


def test_xor_obfuscator():
    code = "test"
    obfuscated = obfuscate('xor', code, key=42)
    deobfuscated = deobfuscate('xor', obfuscated, key=42)
    assert deobfuscated == code


def test_minify_obfuscator():
    code = "x = 5\ny = 10"
    obfuscated = obfuscate('minify', code)
    assert '\n' not in obfuscated


def test_arithmetic_obfuscator():
    code = "x = 5"
    obfuscated = obfuscate('arithmetic', code)
    assert obfuscated != code


def test_function_rename():
    code = "def test_func():\n    pass"
    obfuscated = obfuscate('function_rename', code, length=8)
    assert 'test_func' not in obfuscated or obfuscated == code


def test_class_rename():
    code = "class MyClass:\n    pass"
    obfuscated = obfuscate('class_rename', code, length=8)
    assert 'MyClass' not in obfuscated or obfuscated == code
