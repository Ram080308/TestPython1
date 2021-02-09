
import time

from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException

driver = webdriver.Chrome("E:\pythonProject\Framefork1\BrowserDrivers\chromedriver.exe")
driver.maximize_window()
driver.get("https://admin-demo.nopcommerce.com/Admin/Customer/List")
driver.find_element_by_xpath("/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/input").click()

time.sleep(5)
table = driver.find_element_by_xpath("(//table[@class='table table-bordered table-hover table-striped dataTable no-footer'])[2]")
body = table.find_element_by_tag_name("tbody")
cells = body.find_elements_by_tag_name("td")
rows = body.find_elements_by_tag_name("tr")
links = driver.find_elements_by_xpath("//i[@class='fa fa-pencil']")
print(len(rows))






