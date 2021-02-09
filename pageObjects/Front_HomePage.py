import time

from selenium import webdriver
from selenium.webdriver import ActionChains



class Front_HomePage:

    women_tab_xpath = "//a[@title='Women']"
    womenTshirts_link_xpath = "(//a[@title='T-shirts'])[1]"


    def __init__(self , driver):
        self.driver = driver

    def test_select_item_womens_tshirt (self):
        womenstab = self.driver.find_element_by_xpath(self.women_tab_xpath)
        actions = ActionChains(self.driver)
        actions.move_to_element(womenstab).perform()
        self.driver.find_element_by_xpath(self.womenTshirts_link_xpath).click()




