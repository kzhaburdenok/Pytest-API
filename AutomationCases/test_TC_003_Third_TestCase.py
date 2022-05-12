import pytest

@pytest.fixture(scope="module")
def fixture_code():
    print("\nThis is the fixture which will be executed before all test cases")
    print("-----------------------------")
    yield 
    print("\nEnd of all test cases..")

actual_result = "Testing"

a = 101
#@pytest.mark.skipif(a>100, reason='skipping as this func is not working')
@pytest.mark.new()
def test_tc_001_login_logout_testing(fixture_code):
    print("\nkek")
    assert not actual_result == "Hello", f"{actual_result} is the same as Hello"

@pytest.mark.new()
@pytest.mark.necessary()
def test_tc_003_login_logout_ivalid_credentials(fixture_code):
    print("\nkek3")
