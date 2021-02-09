import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.HomePage import HomePage
from pageObjects.Manufacturers_Create import Manufacturers
from utilities.readConfig import ReagConfig
from utilities import ExcelUtility


class Test_006_Add_New_Manufacturer:

    baseurl = ReagConfig.getApplicationUrl()

    path = ".//TestData/TestData_NopAdmin.xlsx"
    sheetname = "LoginDetails"

    rowcount = ExcelUtility.getRowcount(path , sheetname)
    username = ExcelUtility.readData(path , sheetname, rowcount, 1)
    password = ExcelUtility.readData(path , sheetname, rowcount, 2)

    @pytest.mark.sanity
    def test_add_new_manufacturer(self, setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseurl)

        self.lp = LoginPage(self.driver)
        self.lp.test_loginToApplication(self.username, self.password)

        self.hp = HomePage(self.driver)
        self.hp.test_click_add_manufacturer()

        self.mp = Manufacturers(self.driver)
        self.mp.test_add_manufacturers_details("Thomas" , "From Indian Steels")

        self.driver.close()

















