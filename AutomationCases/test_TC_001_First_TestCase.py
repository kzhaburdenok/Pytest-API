import pytest

a = 101
#@pytest.mark.skipif(a>100, reason='skipping as this func is not working')
@pytest.mark.new()
def test_tc_001_login_logout_testing():
    print("\nkek")

@pytest.mark.new()
@pytest.mark.necessary()
def test_tc_003_login_logout_ivalid_credentials():
    print("\nkek3")
