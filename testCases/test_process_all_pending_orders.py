import pytest
from selenium import webdriver
from utilities.readConfig import ReagConfig
from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from pageObjects.OrdersPage import OrderPage

class Test_004_process_pending_orders:

    baseurl = ReagConfig.getApplicationUrl()
    username = ReagConfig.getUserName()
    password = ReagConfig.getPassword()
    orderstatus = "Pending"
    after_orderStatus = "Complete"

    @pytest.mark.regerssion
    def test_process_pending_orders(self , setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.hp = LoginPage(self.driver)
        self.hp.test_loginToApplication(self.username, self.password)

        self.hp = HomePage(self.driver)
        self.hp.clickOrdersLink()

        self.op = OrderPage(self.driver)
        self.op.test_updateOrderStatus(self.orderstatus, self.after_orderStatus)


