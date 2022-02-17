from covidwtf import get_cases_int

def test_get_cases_int():
    assert get_cases_int("1 2 3") == 123
    assert get_cases_int("4 5 6") == 456
    assert get_cases_int("foo") == False
