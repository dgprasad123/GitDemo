import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="E:\chromedriver_win32\chromedriver.exe")
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="E:\geckodriver-v0.32.0-win64\geckodriver.exe")
    elif browser_name == "IE":
        print("IE Driver")

    driver.get("https://www.rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()

    request.cls.driver = driver
    yield
    driver.close()

