from selenium import webdriver
import time


driver = webdriver.Chrome()
driver.get("https://www.mpl.live/pool")
driver.maximize_window()

msg = input("Enter The Number:-  ")
count = int(input("Enter Count:-  "))

msg_box = driver.find_element_by_xpath("//*[@id='mobile']")

for index in range(count):
    time.sleep(5)
    msg_box.send_keys(msg)

    driver.find_element_by_xpath("//*[@id='sms-but']").click()

print("success")

