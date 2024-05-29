from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#to keep our tab open even after program execution
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

number=driver.find_element(By.CSS_SELECTOR,value="#articlecount a")
print(number.text)

# number.click()

content_link=driver.find_element(By.LINK_TEXT,value="Content portals")
# content_link.click()

search=driver.find_element(By.NAME,value="search")
# for sending any text in forms
search.send_keys("Python")

# but in order to send something like enter, tab or fucntionality we use the above Keys module from common.keys

search.send_keys(Keys.ENTER)



# driver.quit()