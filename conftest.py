import pytest
"""
Scopes: "session", "package", "module", "class", "function"
"""
@pytest.fixture(scope="function")
def prework():
    print(f"before test\n")