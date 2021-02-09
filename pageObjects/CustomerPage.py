
from selenium import webdriver

class CustomerPage:

    button_AddNew_Xpath = "/html/body/div[3]/div[3]/div/form[1]/div[1]/div/a"

    def __init__(self,driver):
        self.driver = driver

    def test_clickAddNewButton(self):
        self.driver.find_element_by_xpath(self.button_AddNew_Xpath).click()


