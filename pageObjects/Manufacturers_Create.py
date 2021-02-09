import time
from selenium import webdriver
#driver = webdriver.Chrome()


class Manufacturers:

    addnew_button_xpath = "//a[@class='btn bg-blue']"
    name_field_xpath = "//input[@id='Name']"
    description_field_xpath = "//body[@id='tinymce']"
    save_button_xpath = "//button[@name='save']"
    frameID = "Description_ifr"

    def __init__(self,driver):
        self.driver = driver

    def test_add_manufacturers_details(self, mname, mdescription):
        self.driver.find_element_by_xpath(self.addnew_button_xpath).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(self.name_field_xpath).send_keys(mname)
        self.driver.switch_to_frame(self.frameID)
        self.driver.find_element_by_xpath(self.description_field_xpath).send_keys(mdescription)
        self.driver.switch_to_default_content()
        self.driver.find_element_by_xpath(self.save_button_xpath).click()




