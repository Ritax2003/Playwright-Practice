import pytest

@pytest.fixture(scope='module')
def preWork():
    print("inside perWork")
    return "true"

def test_init(preWork):
    print(f"inside test_init")
    assert preWork == 'true'