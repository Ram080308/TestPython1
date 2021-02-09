
import time
from selenium import webdriver

driver = webdriver.Chrome("E:\pythonProject\Framefork1\BrowserDrivers\chromedriver.exe")
driver.maximize_window()

driver.get("https://admin-demo.nopcommerce.com/Admin/Order/List")
driver.find_element_by_xpath("//input[@type='submit']").click()

# Find the table
table = driver.find_element_by_xpath("//table[@id='orders-grid']")
body = table.find_element_by_tag_name("tbody")
rows = body.find_elements_by_tag_name("tr")
links = driver.find_elements_by_xpath("//a[@class='btn btn-default']")

time.sleep(4)
print(len(rows))

# Get all the links to be clicked into the list
links_to_click = []

for i in range(len(rows)):
    col = rows[i].find_elements_by_tag_name("td")
    for j in range(len(col)):
        if col[j].text == "Pending":
            links_to_click.append(links[i].get_attribute('href'))


print(links_to_click)

for link in links_to_click:
    driver.get(link)
    driver.back()

