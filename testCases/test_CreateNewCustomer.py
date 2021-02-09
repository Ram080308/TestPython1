import time
import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.HomePage import HomePage
from utilities import readConfig, ExcelUtility
from utilities.readConfig import ReagConfig
from testCases.conftest import setup
from pageObjects.CustomerPage import CustomerPage
from pageObjects.AddNewCustomerPage import AddNewCustomer

class Test_002_AddCustomer:

    baseurl = ReagConfig.getApplicationUrl()
    path = ".//TestData/TestData_NopAdmin.xlsx"
    sheetname = "LoginDetails"
    sheetname_create_profile = "ProfileDetails"

    # Login details
    rowcount = ExcelUtility.getRowcount(path, sheetname)
    username = ExcelUtility.readData(path, sheetname, rowcount, 1)
    password = ExcelUtility.readData(path, sheetname, rowcount, 2)

    # Register details

    email = ExcelUtility.readData(path,sheetname_create_profile,2, 1)
    password_create_profile = ExcelUtility.readData(path,sheetname_create_profile,2, 2)
    firstname = ExcelUtility.readData(path, sheetname_create_profile, 2, 3)
    lastname = ExcelUtility.readData(path, sheetname_create_profile, 2, 4)
    gender = ExcelUtility.readData(path, sheetname_create_profile, 2, 5)
    dob = ExcelUtility.readData(path, sheetname_create_profile, 2, 6)
    strval = str(dob)
    ret = strval.split(" ")
    getdob = ret[0]
    print("Get DOB = " , getdob)



    @pytest.mark.regression
    def test_addCustomer(self, setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.test_loginToApplication(self.username , self.password)

        self.hp = HomePage(self.driver)
        self.hp.clickCustomerLink()

        self.cp = CustomerPage(self.driver)
        self.cp.test_clickAddNewButton()

        self.anc = AddNewCustomer(self.driver)
        self.anc.test_register_user(self.email, self.password, self.firstname, self.lastname, self.gender, self.getdob)
        self.driver.close()






















