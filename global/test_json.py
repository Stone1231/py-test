# import pytest

# @pytest.fixture(scope='session')
# def json_data(data):
#     return data


def test_json(global_json):
    name = global_json['name']
    print(name)
    assert name == "stone"
