from src.service import calculate


def test_add():
    assert calculate("add", 7, 5) == 12


def test_multiply():
    assert calculate("multiply", 7, 5) == 35
