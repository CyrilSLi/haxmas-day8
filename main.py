from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.common import exceptions
import time

driver = webdriver.Chrome()
driver.get("https://ozh.github.io/cookieclicker/")
start_time = time.time()

def when_exists(by, identifier):
    while not driver.find_elements(by, identifier):
        pass
    return driver.find_element(by, identifier)

def upgrade(element_id):
    while True:
        try:
            driver.find_element(By.ID, element_id).click()
            break
        except (exceptions.StaleElementReferenceException, exceptions.NoSuchElementException):
            pass

when_exists(By.ID, "langSelect-EN").click()
try:
    when_exists(By.ID, "prefsButton").click()
except exceptions.StaleElementReferenceException:
    when_exists(By.ID, "prefsButton").click()

while True:
    close = when_exists(By.CLASS_NAME, "close")
    try:
        close.click()
    except exceptions.ElementNotInteractableException:
        break
while True:
    try:
        when_exists(By.CLASS_NAME, "cc_btn_accept_all").click()
        break
    except exceptions.ElementNotInteractableException:
        pass

for pref in ("fancyButton", "filtersButton", "particlesButton", "numbersButton"):
    try:
        button = when_exists(By.ID, pref).click()
    except exceptions.ElementClickInterceptedException:
        print("Could not click", pref)
        pass

cookie_el = when_exists(By.ID, "bigCookie")
click_delay = 0.019

action = ActionChains(driver).click(cookie_el)
start_section_time = time.time()
for _ in range(15): # Cursor
    action = action.pause(click_delay).click()
action.perform()
upgrade("product0")
for _ in range(102): # Reinforced index finger
    action = action.pause(click_delay).click()
action.perform()
upgrade("upgrade0")
for _ in range(255): # Carpal tunnel prevention cream
    action = action.pause(click_delay).click()
action.perform()
upgrade("upgrade0")
section_time = time.time() - start_section_time
for _ in range(int(375 / section_time * (60 - section_time))):
    action = action.pause(click_delay).click()
action.perform()
while (time.time() - start_time) < 60:
    cookie_el.click()

end_time = time.time()
cookies = int(when_exists(By.ID, "cookies").text.split()[0].strip().replace(",", ""))
print("Time elapsed:", end_time - start_time)
print("Cookies:", cookies)
print("Cookies per second: ", cookies / (end_time - start_time))
driver.quit()

