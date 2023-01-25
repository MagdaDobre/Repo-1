from browser import Browser
from selenium.webdriver.common.by import By
from time import sleep

class Home_Page(Browser):

    FORGOT_PASSWORD_LINK = (By.LINK_TEXT, "Forgot Password")
    FORM_AUTH_LINK = (By.XPATH, '//a[@href = "/login"]')
    ENTRY_AD = (By.XPATH, '//a[@href ="/entry_ad"]')
    TYPOS = (By.XPATH, '//a[@href ="/typos"]')


    def navigate_to_home_page(self):
        self.driver.get("https://the-internet.herokuapp.com/")

    def forgot_password(self):
        self.driver.find_element(*self.FORGOT_PASSWORD_LINK).click()
        sleep(3)

    def form_auth(self):
        self.driver.find_element(*self.FORM_AUTH_LINK).click()
        sleep(3)

    def entry_ad(self):
        self.driver.find_element(*self.ENTRY_AD).click()
        sleep(3)

    def typos(self):
        self.driver.find_element(*self.TYPOS).click()