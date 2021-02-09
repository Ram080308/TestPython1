
from selenium import webdriver

class LoginPage:
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_submit_xpath = "//input[@type='submit']"
    link_Logout_LinkText = "Logout"
    link_Customers_xpath = "(//span[text()='Customers'])[1]"
    link_Customers_inside_xpath = "(//span[text()='Customers'])[2]"

    def __init__(self,driver):
        self.driver = driver

    def test_loginToApplication(self, username, password):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)
        self.driver.find_element_by_xpath(self.button_submit_xpath).click()


