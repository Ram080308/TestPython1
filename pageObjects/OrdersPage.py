import time
from selenium import webdriver
from selenium.webdriver.support.select import Select

class OrderPage:
    view_links_xpath = "//a[@class='btn btn-default']"
    table_webtable_xpath = "//table[@id='orders-grid']"
    payment_status_Paid_xpath = "(//li[text()='Paid'])[1]"
    search_button_xpath = "//button[@id='search-orders']"
    button_changeorderstatus_xpath = "//button[@name='btnChangeOrderStatus']"
    dropdown_orderstatus_xpath = "//select[@name='OrderStatusId']"
    button_save_xpath = "//button[@id='btnSaveOrderStatus']"
    link_backtoorder_xpath = "back to order list"
    button_Yes_xpath = "//*[@id='btnSaveOrderStatus-action-confirmation-submit-button']"

    def __init__(self, driver):
        self.driver = driver

    def test_updateOrderStatus(self , orderStatus, order_status):

        self.driver.find_element_by_xpath(self.payment_status_Paid_xpath)
        self.driver.find_element_by_xpath(self.search_button_xpath)

        allviewlinks =  self.driver.find_elements_by_xpath(self.view_links_xpath)

        table = self.driver.find_element_by_xpath(self.table_webtable_xpath)
        body = table.find_element_by_tag_name("tbody")
        rows = body.find_elements_by_tag_name("tr")
        get_all_viewlinks = []

        for i in range(len(rows)):
            col = rows[i].find_elements_by_tag_name("td")
            for j in range(len(col)):
               if col[j].text == orderStatus:
                   get_all_viewlinks.append(allviewlinks[i].get_attribute('href'))

        for links in get_all_viewlinks:
            self.driver.get(links)
            self.driver.find_element_by_xpath(self.button_changeorderstatus_xpath).click()
            dropdown = self.driver.find_element_by_xpath(self.dropdown_orderstatus_xpath)
            self.ordstatus = Select(dropdown)
            time.sleep(3)
            self.ordstatus.select_by_visible_text(order_status)
            self.driver.find_element_by_xpath(self.button_save_xpath).click()
            time.sleep(2)
            self.driver.find_element_by_xpath(self.button_Yes_xpath).click()
            self.driver.find_element_by_link_text(self.link_backtoorder_xpath).click()















