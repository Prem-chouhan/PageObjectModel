from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://www.linkedin.com/home")
driver.find_element_by_xpath("/html/body/nav/a[3]").click()
driver.find_element_by_xpath("/html/body/div/main/div/form/div[1]/input").send_keys("wankhadechetan281@gmail.com")
driver.find_element_by_xpath("//*[@id='password']").send_keys("Chetan@95")
driver.find_element_by_xpath("//*[@id='app__container']/main/div/form/div[3]/button").click()
print(driver.title)