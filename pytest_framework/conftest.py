import pytest
# create conf for pytest, setuop, tear, html,
@pytest.fixture()# function
def start1():
    print("this is setup`1")
    # return True, True
    yield True, True
    print("this is teardown`1")

@pytest.fixture()
def start2():
    print("this is setup 2")
    yield
    print("this is teardown`2")

@pytest.fixture(scope='class')
def start3():
    print("this is setup 3")
    yield
    print("this is teardown`3")

@pytest.fixture(scope='module')
def start4():
    print("this is setup 4")
    yield
    print("this is teardown`4")

#################3markers

def pytest_configure(config):
    config.addinivalue_line("markers", "functionality: functional testing")
    config.addinivalue_line("markers", "regression: regression testing")


