import time


class FinalCheckout:
    proceedCheckout_button_xpath = "//button[@class='button btn btn-default button-medium']"
    tandc_chkbox_xpath = "//input[@type='checkbox']"
    prced_chk_xpath = "//*[@id='form']/p/button"
    payment_link_xpath = "//a[@title='Pay by check.']"
    confirmOder_button_xpath = "//span[text()='I confirm my order']"


    def __init__(self, driver):
        self.driver = driver

    def test_complete_checkout(self):
        self.driver.find_element_by_xpath(self.proceedCheckout_button_xpath).click()
        self.driver.find_element_by_xpath(self.tandc_chkbox_xpath).click()
        time.sleep(4)
        self.driver.find_element_by_xpath(self.prced_chk_xpath).click()
        time.sleep(4)
        self.driver.find_element_by_xpath(self.payment_link_xpath).click()
        time.sleep(4)
        self.driver.find_element_by_xpath(self.confirmOder_button_xpath).click()



