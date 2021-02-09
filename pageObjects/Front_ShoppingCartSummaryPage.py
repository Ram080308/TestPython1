import time

from selenium import webdriver

class ShoppingCartsummary:
    proceedtocheckout_button_xpath = "//span[text()='Proceed to checkout']"
    viewshoppingcart_link_xpath = "//a[@title='View my shopping cart']"

    def __init__(self , driver):
        self.driver = driver

    def test_proceed_to_checkout(self):
        self.driver.refresh()
        time.sleep(3)
        self.driver.find_element_by_xpath(self.proceedtocheckout_button_xpath).click()

