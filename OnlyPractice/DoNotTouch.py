import time
from selenium import webdriver

driver = webdriver.Chrome("E:\pythonProject\Framefork1\BrowserDrivers\chromedriver.exe")
driver.maximize_window()

driver.get("https://admin-demo.nopcommerce.com/Admin/Customer/List")
driver.find_element_by_xpath("//input[@type='submit']").click()

time.sleep(5)
table = driver.find_element_by_xpath("(//table[@class='table table-bordered table-hover table-striped dataTable no-footer'])[2]")
body = table.find_element_by_tag_name("tbody")
cells = body.find_elements_by_tag_name("td")
rows = body.find_elements_by_tag_name("tr")
#links = driver.find_elements_by_xpath("//i[@class='fa fa-pencil']")
links = driver.find_elements_by_xpath("//a[@class='btn btn-default']")

print(len(rows))

# -- first get all links ---

links_to_click = []

for i in range(len(rows)):
    col = rows[i].find_elements_by_tag_name("td")
    for j in range(len(col)):
        if col[j].text == "Registered":
            links_to_click.append(links[i].get_attribute('href'))

print(links_to_click)

# --- next visit all links ---

for link in links_to_click:
    driver.get(link)
    #driver.find_element_by_link_text("back to customer list").click()