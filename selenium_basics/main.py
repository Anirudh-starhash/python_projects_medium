from selenium import webdriver
from selenium.webdriver.common.by import By

#to keep our tab open even after program execution
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org")

event_times=driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
event_names=driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
event={}

for x in range(len(event_times)):
    event[x]={
        "name":event_names[x].text,
        "time":event_times[x].text,
    }
    
    
print(event,sep="\n")
# driver.close()
driver.quit()



