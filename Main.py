from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("https://orteil.dashnet.org/cookieclicker/")

driver.implicitly_wait(5)

lang = driver.find_element(By.ID, "langSelect-EN")

lang.click()

try:
    main = WebDriverWait(driver, 50).until(
        EC.presence_of_element_located((By.ID, "bigCookie"))
    )
finally:
    cookie = driver.find_element(By.ID, "bigCookie")
    cookie_count = driver.find_element(By.ID, "cookies")
    items = [driver.find_element(By.ID, "productPrice"+str(i))for i in range(1,-1,-1)]

driver.implicitly_wait(5)
for i in range(5000):
    cookie.click()
    no = cookie_count.text.split(" ")[0]
    count = int(no.replace(',',''))
    print(count)
    for item in items:
        value = int(item.text)
        if value <= count:
            upgrade_actions = ActionChains(driver)
            upgrade_actions.move_to_element(item)
            upgrade_actions.click()
            upgrade_actions.perform()

driver.implicitly_wait(15)
driver.quit()

