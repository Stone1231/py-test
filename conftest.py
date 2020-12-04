import pytest
import json


def pytest_addoption(parser):
    parser.addoption("--file", action="store", help="provide a json file path")


def read_json(request):
    path = request.config.getoption("--file")
    if path is None:
        path = 'data.json'
    file = open(path)
    data = json.load(file)
    return data


#Read url and header config from json file
@pytest.fixture(scope="session", autouse=True)
def global_json(request):
    print('\nRead config from json file!')
    header_dict = read_json(request)
    return header_dict


@pytest.fixture
def global_value():
    return "global"
