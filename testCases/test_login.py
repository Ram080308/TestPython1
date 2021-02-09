import pytest
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import Logen
from utilities.readConfig import ReagConfig
from utilities import ExcelUtility


class Test_001_Login_To_NopCommerce_Admin:

    baseurl = ReagConfig.getApplicationUrl()

    path = ".//TestData/TestData_NopAdmin.xlsx"
    sheetname = "LoginDetails"

    rowcount = ExcelUtility.getRowcount(path , sheetname)
    username = ExcelUtility.readData(path , sheetname, rowcount, 1)
    password = ExcelUtility.readData(path , sheetname, rowcount, 2)

    @pytest.mark.sanity
    def test_login_nop_portal(self, setup):

        self.driver = setup
        self.driver.get(self.baseurl)
        self.lp = LoginPage(self.driver)

        self.lp.test_loginToApplication(self.username, self.password)
        self.driver.close()













