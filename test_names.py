from names import make_full_name, extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    assert make_full_name("Carlos","Reyes") == "Reyes; Carlos"

def test_extract_family_name():
    assert extract_family_name("Reyes; Carlos") == "Reyes"

def test_extract_given_name():
    assert extract_given_name("Reyes; Carlos") == "Carlos"

pytest.main(["-v", "--tb=line", "-rN", __file__])
