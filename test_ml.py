import pytest
# TODO: add necessary import

# TODO: implement the first test. Change the function name and input as needed
def test_setup():
    """
    Basick check to ensure test are running
    """
    assert True


# TODO: implement the second test. Change the function name and input as needed
def test_environment():
    """
    Verify pyton enviorment is accessible
    """
    import sys
    assert sys.version_info >=(3,8)


# TODO: implement the third test. Change the function name and input as needed
def test_logic():
    """
    A placeholder for ML logic test
    """
    expected = 4
    assert 2 + 2 == expected
