from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    full=make_full_name("Juan", "Gomez")
    assert isinstance (full, str)
    assert make_full_name("Juan", "Gomez")=="Gomez; Juan"
    assert make_full_name("Christopher", "Colombus")=="Colombus; Christopher"
    assert make_full_name("Eduardo", "Ruiz-Tagle")=="Ruiz-Tagle; Eduardo"

def test_extract_family_name():
    full=extract_family_name("Gomez; Juan")
    assert isinstance (full, str)
    assert extract_family_name('Gomez; Juan')=="Gomez"
    assert extract_family_name("Colombus; Christopher")=="Colombus"
    assert extract_family_name("Ruiz-Tagle; Eduardo")=="Ruiz-Tagle"

def test_extract_given_name():
    full=extract_given_name("Gomez; Juan")
    assert isinstance (full, str)
    assert extract_given_name('Gomez; Juan')=="Juan"
    assert extract_given_name("Colombus; Christopher")=="Christopher"
    assert extract_given_name("Ruiz-Tagle; Eduardo")=="Eduardo"

pytest.main(["-v", "--tb=line", "-rN", __file__])

