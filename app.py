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

form1 = driver.find_element(By.ID, 'wpforms-8-field_4')
form1.clear()
form1.send_keys('Michael Scott')

form2 = driver.find_element(By.ID, 'wpforms-8-field_1')
form2.clear()
form2.send_keys('Mscott@papercompany.com')

form3 = driver.find_element(By.ID, 'wpforms-8-field_3')
form3.clear()
form3.send_keys('Need a Website')

form4 = driver.find_element(By.ID, 'wpforms-8-field_2')
form4.clear()
form4.send_keys('Hi, I need help with a website. I could use a quote for the work.')

btn = driver.find_element(By.ID, 'wpforms-submit-8')
btn.click()

driver.back()


time.sleep(5)
driver.quit()









# element = driver.find_element(
#     By.XPATH, '//*[@id="menu-item-121"]/a')

# actions = ActionChains(driver)
# actions.click(element)
# actions.perform()