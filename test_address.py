from address import extract_city, extract_state, extract_zipcode
import pytest

def test_extract_city():
    full=extract_city("525 S Center St, Rexburg, ID 83460")
    assert isinstance (full, str)
    assert extract_city("525 S Center St, Rexburg, ID 83460")==approx("Rexburg")

def test_extract_state():
    full=extract_state("525 S Center St, Rexburg, ID 83460")
    assert isinstance (full, str)
    assert extract_state("525 S Center St, Rexburg, ID 83460")==approx("ID")

def test_extract_zipcode():
    full=extract_zipcode("525 S Center St, Rexburg, ID 83460")
    assert isinstance (full, str)
    assert extract_zipcode("525 S Center St, Rexburg, ID 83460")==approx("83460")

pytest.main(["-v", "--tb=line", "-rN", __file__])