from selenium import webdriver
from selenium.webdriver.common.keys import Keys

running = True
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://monkeytype.com")

input = driver.find_element_by_id("wordsInput")

while running == True:
    activeWord = driver.find_element_by_class_name("word.active")
    input.send_keys(activeWord.text)
    input.send_keys(Keys.SPACE)
