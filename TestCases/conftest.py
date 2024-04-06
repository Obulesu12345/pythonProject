# from selenium import webdriver
# import configparser
# from utilities import ReadConfiguration
# import utilities
# import pytest
# @pytest.fixture()
# def setup_and_teardown(request):
#     browser = ReadConfiguration.read_configuration("basic info","browser")
#     driver = webdriver.Chrome()
#     if browser.__eq__("chrome"):
#         driver = webdriver.Chrome()
#     elif browser.__eq__("firefox"):
#         driver = webdriver.Firefox()
#     elif browser.__eq__("edge"):
#         driver = webdriver.Edge()
#     else:
#         print("please provide a valid browser name from this list chrome/firefox/edge")
#     driver.maximize_window()
#     driver.get("https://dev.zybisys.com/login")
#     request.cls.driver = driver
#     yield
#     driver.quit()



from selenium import webdriver
from utilities import ReadConfiguration
import pytest
@pytest.fixture()
def setup_and_teardown(request):
    browser = ReadConfiguration.read_configuration("basic info","browser")
    driver = webdriver.Chrome()
    if browser.__eq__("chrome"):
        driver = webdriver.Chrome()
    elif browser.__eq__("firefox"):
        driver = webdriver.Firefox()
    elif browser.__eq__("edge"):
        driver = webdriver.Edge()
    else:
        print("please provide a valid browser name from this list chrome/firefox/edge")
    driver.maximize_window()
    driver.get("https://dev.zybisys.com/login")
    request.cls.driver = driver
    yield
    driver.quit()

