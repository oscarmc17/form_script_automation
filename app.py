from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()

driver.get("https://oscardevelops.com/")

element = driver.find_element(
    By.XPATH, '//*[@id="menu-item-121"]/a')


actions = ActionChains(driver)
actions.click(element)
actions.perform()
