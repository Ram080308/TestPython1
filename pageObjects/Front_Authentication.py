import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AuthenticationPage:

    emailid_textbox_xpath = "//input[@id='email_create']"
    time.sleep(3)
    createaccount_button_xpath = "//i[@class='icon-user left']"

    gender_radio_xpath = "//*[@id='uniform-id_gender1']"
    firstname_textbox_xpath = "//input[@id='customer_firstname']"
    lastname_textbox_xpath = "//input[@id='customer_lastname']"
    password_textbox_xpath = "//input[@id='passwd']"
    address_textbox_xpath = "//input[@id='address1']"
    city_textbox_xpath = "//input[@id='city']"
    states_dropdown_xpath = "//select[@id='id_state']"
    zipcode_textbox_xpath = "//input[@id='postcode']"
    country_dropdown_xpath = "//select[@id='id_country']"
    mobile_textbox_xpath = "//input[@id='phone_mobile']"
    addressalias_textbox_xpath = "//input[@id='alias']"
    register_button_xpath = "//span[text()='Register']"

    def __init__(self, driver):
        self.driver = driver

    def test_checkout_create_account (self):
        self.driver.find_element_by_xpath(self.emailid_textbox_xpath).send_keys("myb11ot109814@ban.com")
        self.driver.find_element_by_xpath(self.createaccount_button_xpath).click()

        time.sleep(5)
        wait = WebDriverWait (self.driver, 20)
        wait.until(EC.element_to_be_clickable((By.XPATH, self.register_button_xpath)))

        self.driver.find_element_by_xpath(self.gender_radio_xpath).click()
        self.driver.find_element_by_xpath(self.firstname_textbox_xpath).send_keys("Ram")
        self.driver.find_element_by_xpath(self.lastname_textbox_xpath).send_keys("Chigari")
        self.driver.find_element_by_xpath(self.password_textbox_xpath).send_keys("Shonya@1223")
        self.driver.find_element_by_xpath(self.address_textbox_xpath).send_keys("Office center drive")
        self.driver.find_element_by_xpath(self.city_textbox_xpath).send_keys("Bangalore")

        stateelement = self.driver.find_element_by_xpath(self.states_dropdown_xpath)
        states = Select(stateelement)
        states.select_by_visible_text("Arkansas")

        self.driver.find_element_by_xpath(self.zipcode_textbox_xpath).send_keys("10112")

        countryelement = self.driver.find_element_by_xpath(self.country_dropdown_xpath)
        country = Select(countryelement)
        country.select_by_visible_text("United States")

        self.driver.find_element_by_xpath(self.mobile_textbox_xpath).send_keys("8554758589")
        self.driver.find_element_by_xpath(self.addressalias_textbox_xpath).send_keys("home")
        self.driver.find_element_by_xpath(self.register_button_xpath).click()








