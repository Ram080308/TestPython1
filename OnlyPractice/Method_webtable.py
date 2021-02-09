
import time
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support import expected_conditions as E
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("E:\pythonProject\Framefork1\BrowserDrivers\chromedriver.exe")
driver.maximize_window()
driver.get("https://admin-demo.nopcommerce.com/Admin/Customer/List")
driver.find_element_by_xpath("/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/input").click()
time.sleep(5)
wait_time_out = 15
wait_variable = W (driver, wait_time_out)

link_view_xpath = "//i[@class='fa fa-pencil']"
allviewlinks = wait_variable.until(E.visibility_of_any_elements_located((By.XPATH , link_view_xpath)))
allview = driver.find_elements_by_xpath(link_view_xpath)
print(len(allviewlinks))

for i in range(len(allviewlinks)):
    try:
        allviewlinks = wait_variable.until(E.visibility_of_any_elements_located((By.XPATH, link_view_xpath)))
        allview[i].click()
        driver.back()
        time.sleep(5)
    except StaleElementReferenceException as E:
        allview[i].click()


