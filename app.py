from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
# from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
driver.get("https://oscardevelops.com/")
print(driver.title)

element = driver.find_element(By.CSS_SELECTOR, "#ast-desktop-header > div > div > div > div > div.site-header-primary-section-right.site-header-section.ast-flex.ast-grid-right-section > div.ast-builder-layout-element.ast-flex.site-header-focus-item.ast-header-button-1 > div > a.ast-custom-button-link")
element.click()
# element.send_keys(Keys.RETURN)


time.sleep(5)
driver.quit()









# element = driver.find_element(
#     By.XPATH, '//*[@id="menu-item-121"]/a')

# actions = ActionChains(driver)
# actions.click(element)
# actions.perform()