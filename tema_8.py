
from time import sleep

import span as span
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

chrome = webdriver.Chrome()
chrome.maximize_window()

chrome.get('https://phptravels.net/')

sleep(3)

# 3 elemente de tip ID


chrome.find_element(By.ID, 'currency').click()
sleep(3)
chrome.find_element(By.ID, 'currency').click()   # pus de 2 ori ca sa inchida drop-downul de mai sus si sa treaca mai departe

chrome.find_element(By.ID, 'languages').click()
sleep(3)

chrome.find_element(By.ID, 'languages').click()  # pus de 2 ori ca sa inchida drop-downul de mai sus si sa treaca mai departe

chrome.find_element(By.ID, 'ACCOUNT').click()

sleep(3)


# ----------------------------------------------------------------
# 3 elemente de tip LINK TEXT
chrome.find_element(By.LINK_TEXT, 'Customer Login').click()
sleep(3)

chrome.find_element(By.LINK_TEXT, 'Hotels').click()
sleep(3)

chrome.find_element(By.LINK_TEXT, 'Tours').click()
sleep(3)

# --------------------------------
# 3 elemente de tip PARTIAL LINK TEXT

chrome.find_element(By.PARTIAL_LINK_TEXT, 'Transf').click()
sleep(3)

chrome.find_element(By.PARTIAL_LINK_TEXT, 'Offe').click()
sleep(3)

chrome.find_element(By.PARTIAL_LINK_TEXT, 'Compa').click()
sleep(3)
chrome.quit()

# ----------------------------------------------
# 3 elemente de tip NAME

chrome.get('https://phptravels.net/flights')

sleep(3)

chrome.find_element(By.NAME, "from").send_keys("Romania")
sleep(3)

chrome.find_element(By.NAME, "to").send_keys("Spain")
sleep(3)

chrome.find_element(By.ID, 'ACCOUNT').click()
chrome.find_element(By.LINK_TEXT, 'Customer Login').click()
chrome.find_element(By.NAME, "email").send_keys("test@test.com")
sleep(3)
chrome.quit()

# -----------------------------------------------------------
# 3 elemente de tip TAG
chrome.get('https://formy-project.herokuapp.com/form')

lista = chrome.find_elements(By.TAG_NAME, 'input')

lista[0].send_keys('Andrei')
lista[1].send_keys('Gheorghe')
lista[2].send_keys('Consultant')

print(lista)
sleep(3)

# ---------------------------------------------------------------
# 3 elemente de tip CLASS NAME
chrome.get('https://phptravels.net/login')

sleep(3)

chrome.find_elements(By.CLASS_NAME, 'form-control')[0].send_keys('test@test.com')
chrome.find_elements(By.CLASS_NAME, 'form-control')[1].send_keys('passtest')
sleep(3)
chrome.find_element(By.CLASS_NAME, 'ladda-label').click()
sleep(3)

chrome.quit()

# ----------------------------------------------------
# 3 elemente de tip CSS

chrome.get('https://phptravels.net/signup')
sleep(3)

chrome.find_element(By.ID, 'cookie_stop').click()

chrome.find_element(By.CSS_SELECTOR, "input.form-control").send_keys('Andrei')
sleep(3)

chrome.find_element(By.CSS_SELECTOR, "input[placeholder='Email']").send_keys("test@test.com")
sleep(3)
chrome.find_element(By.CSS_SELECTOR, 'span#select2-account_type-container').click()
sleep(3)

chrome.quit()

# -------------------------------------------------------------------
# XPATH

chrome.get('https://formy-project.herokuapp.com/form')

sleep(3)

chrome.find_element(By.XPATH, "//input[@id='job-title']").send_keys("Consultant")
sleep(3)
chrome.find_element(By.XPATH, "//input[@id='datepicker']").send_keys("09/05/2020")
sleep(3)
chrome.find_element(By.XPATH, "//label['date']").click()
sleep(3)
chrome.find_element(By.XPATH, "//input[@id='checkbox-2']").click()

sleep(3)

chrome.find_element(By.XPATH, "//label[text()='Job title']/parent::strong/following-sibling::input").send_keys('1111111111')

sleep(3)

chrome.quit()


chrome.get('https://www.techlistic.com/p/selenium-practice-form.html')

sleep(3)
chrome.find_element(By.ID, "ez-accept-all").click()
chrome.find_element(By.XPATH, "//option[text() = 'Europe']").click()
sleep(3)
chrome.find_element(By.XPATH, "//option[contains(text(),'Afr')]").click()

sleep(3)

s = chrome.find_element(By.XPATH, "//input[@id='job-title'] | //input[@id='datepicker']")
s.send_keys('test')
sleep(3)
s.clear()

sleep(3)
chrome.find_element(By.XPATH, "//*[option='Europe']").send_keys('E')
sleep(3)
chrome.quit()

chrome.get('https://phptravels.net/')
sleep(3)
chrome.find_element(By.XPATH, '(//a[@class="dropdown-toggle dropdown-btn travellers waves-effect"])[1]').click()

sleep(3)
chrome.quit()

chrome.get('https://formy-project.herokuapp.com/form')
sleep(3)
def formy_input(id_text):
    input = chrome.find_element(By.XPATH, f'//input[@id = "{id_text}"]')
    input.click()


formy_input("radio-button-1")
formy_input('radio-button-2')
sleep(3)
