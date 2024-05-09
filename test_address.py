from names import extract_city, extract_state, extract_zipcode
import pytest


def test_extract_city():
    assert extract_city()

def test_extract_state():
    assert extract_state()

def test_extract_zipcode():
    assert extract_zipcode()



pytest.main(["-v", "--tb=line", "-rN", __file__])
