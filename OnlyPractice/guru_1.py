import time

from selenium import webdriver

driver = webdriver.Chrome("E:\pythonProject\Framefork1\BrowserDrivers\chromedriver.exe")
driver.maximize_window()
driver.get("http://demo.guru99.com/test/web-table-element.php")

table = driver.find_elements_by_xpath("//table[@class='dataTable']")
head = driver.find_element_by_tag_name("thead")
headrows = head.find_elements_by_tag_name("th")
body = driver.find_element_by_tag_name("tbody")
rows = body.find_elements_by_tag_name("tr")
print(len(headrows))
print(len(rows))

for i in range(len(rows)):
    count = 0
    col = rows[i].find_elements_by_tag_name("td")
    for j in range(len(col)):
        time.sleep(3)
        col[count].click()
        driver.back()
        count = count+1

    break


