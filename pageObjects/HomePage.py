import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    link_Logout_LinkText = "Logout"
    link_Customers_xpath = "(//span[text()='Customers'])[1]"
    link_Customers_inside_xpath = "(//span[text()='Customers'])[2]"
    link_Sales_xpath = "//span[text()='Sales']"
    link_Orders_inside_Sales_xpath = "//span[text()='Orders']"
    link_catalog_xpath = "//span[text()='Catalog']"
    link_catagog_manufactures_xpath = "//span[text()='Manufacturers']"

    def __init__(self, driver):
        self.driver = driver

    def clickCustomerLink(self):
        self.driver.find_element_by_xpath(self.link_Customers_xpath).click()
        self.driver.find_element_by_xpath(self.link_Customers_inside_xpath).click()

    def clickOrdersLink(self):
        self.driver.find_element_by_xpath(self.link_Sales_xpath).click()
        self.driver.find_element_by_xpath(self.link_Orders_inside_Sales_xpath).click()

    def test_click_add_manufacturer(self):
        self.driver.find_element_by_xpath(self.link_catalog_xpath).click()
        wait = WebDriverWait(self.driver, 30)
        wait.until(EC.element_to_be_clickable((By.XPATH, self.link_catagog_manufactures_xpath)))
        self.driver.find_element_by_xpath(self.link_catagog_manufactures_xpath).click()

    def clickLogoutLink(self):
        self.driver.find_element_by_link_text(self.link_Logout_LinkText).click()
