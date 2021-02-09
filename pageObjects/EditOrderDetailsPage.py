from selenium import webdriver
from selenium.webdriver.support.select import Select


class EditOrderDetails:
    button_changeorderstatus_xpath = "//button[@name='btnChangeOrderStatus']"
    dropdown_orderstatus_xpath = "//select[@name='OrderStatusId']"
    button_save_xpath = "//button[@id='btnSaveOrderStatus']"
    link_backtoorder_xpath = "back to order list"

    def __init__(self, driver):
        self.driver = driver

    def test_change_order_status(self, order_status):
        self.driver.find_element_by_xpath(self.button_changeorderstatus_xpath)

        dropdown = self.driver.find_element_by_xpath(self.dropdown_orderstatus_xpath)
        self.ordstatus = Select(dropdown)
        self.ordstatus.select_by_visible_text(order_status)

        self.driver.find_element_by_xpath(self.button_save_xpath)
        self.driver.find_element_by_link_text(self.link_backtoorder_xpath)


