import pytest
from selenium import webdriver

@pytest.fixture()
def setup():
    driver = webdriver.Chrome("E:\\pythonProject\\Framefork1\\BrowserDrivers\\chromedriver.exe")
    return driver





