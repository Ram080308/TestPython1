import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Womens_Tshirt_Landing_Page:
    quickview_link_xpath = "//*[@id='center_column']/ul/li/div/div[1]/div/a[1]/img"
    frame_id = "fancybox-frame1612672239806"
    quantity_textfield_xpath = "//*[@id='quantity_wanted']"
    addtocart_button_xpath = "//*[@id='add_to_cart']/button/span"
    proceedtocheckout_button_xpath = "//*[@id='layer_cart']/div[1]/div[2]/div[4]/a"

    def __init__(self , driver):
        self.driver = driver

    def test_add_item_to_cart(self, qty):
        wait = WebDriverWait(self.driver, 20)

        wait.until(EC.element_to_be_clickable((By.XPATH, self.quickview_link_xpath)))
        element = self.driver.find_element_by_xpath(self.quickview_link_xpath)
        self.driver.execute_script("arguments[0].click();", element)

        wait.until(EC.element_to_be_clickable((By.XPATH, self.quantity_textfield_xpath)))
        self.driver.find_element_by_xpath(self.quantity_textfield_xpath).send_keys(qty)
        self.driver.find_element_by_xpath(self.quantity_textfield_xpath).clear()
        self.driver.find_element_by_xpath(self.addtocart_button_xpath).click()

        we = self.driver.find_element_by_xpath(self.proceedtocheckout_button_xpath)
        self.driver.execute_script("arguments[0].click();", we)




