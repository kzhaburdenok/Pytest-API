import pytest

actual_result = "Hello"

a = 101
#@pytest.mark.skipif(a>100, reason='skipping as this func is not working')
@pytest.mark.new()
def test_tc_001_login_logout_testing():
    print("\nkek")
    assert not actual_result == "Hello", f"{actual_result} is the same as Hello"

@pytest.mark.new()
@pytest.mark.necessary()
def test_tc_003_login_logout_ivalid_credentials():
    print("\nkek3")
