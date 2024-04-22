from selenium import webdriver
from utilities.ReadConfiguration import read_configuration
import pytest
@pytest.fixture()
def setup_and_teardown(request):
    browser = read_configuration("basic info","browser")
    driver = None
    if browser.__eq__("chrome"):
        driver = webdriver.Chrome()
    elif browser.__eq__("firefox"):
        driver = webdriver.Firefox()
    elif browser.__eq__("edge"):
        driver = webdriver.Edge()
    else:
        print("please provide a valid browser name from this list chrome/firefox/edge")
    driver.maximize_window()
    # driver.set_page_load_timeout(60)
    # app_url = ReadConfiguration.read_configuration("basic info", "url")
    driver.get("https://dev.zybisys.com/login")
    request.cls.driver = driver
    yield
    driver.quit()