import pytest


@pytest.fixture(scope='session')  # function, class, module, package, session
def hello_world():
    return "hello world"


def test_h_in_hello_world(hello_world):
    assert "h" in hello_world


def test_w_in_hello_world(hello_world, record_testsuite_property):
    record_testsuite_property(
        "name",
        test_w_in_hello_world.__name__ + "[測試test w in hello world 是否正確]")
    assert "w" in hello_world