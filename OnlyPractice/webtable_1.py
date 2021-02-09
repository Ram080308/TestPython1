import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("E:\pythonProject\Framefork1\BrowserDrivers\chromedriver.exe")
driver.maximize_window()
driver.get("http://demo.guru99.com/test/web-table-element.php#")

table = driver.find_element_by_xpath("//table[@class='dataTable']")
head = table.find_elements_by_tag_name("th")
body = table.find_element_by_tag_name("tbody")
cells = body.find_elements_by_tag_name("td")
rows = body.find_elements_by_tag_name("tr")
print(len(rows))

for i in range(len(rows)):
    col = rows[i].find_elements_by_tag_name("td")
    for j in range(len(col)):
        time.sleep(5)
        col[0].click()






