from selenium import webdriver

class AddNewCustomer:
    text_email_xpath = "//input[@id='Email']"
    text_password_xpath = "//input[@id='Password']"
    text_firstname_xpath = "//input[@id='FirstName']"
    text_lastname_xpath = "//input[@id='LastName']"
    radio_gender_male_xpath = "//input[@id='Gender_Male']"
    radio_dender_female_xpath = "//input[@id='Gender_Female']"
    text_dob_xpath = "//input[@id='DateOfBirth']"
    button_save_xpath = "(//button[@type='submit'])[2]"

    def __init__(self , driver):
        self.driver = driver

    def test_register_user(self, email, password, firstname, lastname, gender, dob):
        self.driver.find_element_by_xpath(self.text_email_xpath).send_keys(email)
        self.driver.find_element_by_xpath(self.text_password_xpath).send_keys(password)
        self.driver.find_element_by_xpath(self.text_firstname_xpath).send_keys(firstname)
        self.driver.find_element_by_xpath(self.text_lastname_xpath).send_keys(lastname)
        if gender == "Female":
            self.driver.find_element_by_xpath(self.radio_dender_female_xpath).send_keys(gender)
        elif gender == "Male":
            self.driver.find_element_by_xpath(self.radio_gender_male_xpath).send_keys(gender)
        else:
            self.driver.find_element_by_xpath(self.radio_gender_male_xpath).send_keys(gender)
        self.driver.find_element_by_xpath(self.text_dob_xpath).send_keys(dob)
        self.driver.find_element_by_xpath(self.button_save_xpath).click()

