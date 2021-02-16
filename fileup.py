import webbrowser
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path="C:\drivers\chromedriverwin32\chromedriver.exe")
driver.get('https://www.filedropper.com/')
print(driver.current_url)
driver.maximize_window()


driver.find_element_by_xpath("//*[@id='uploadFile']").send_keys("C://drivers/testup/download.jpg")