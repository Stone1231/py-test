import pytest


def test_value(global_value):
    print(global_value)
    assert "global" == global_value