from browser import Browser
from selenium.webdriver.common.by import By


class Login_Page(Browser):
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.XPATH, '//button/i[text() =" Login"]')


    def navigate_to_login_page(self):
        self.driver.get("https://the-internet.herokuapp.com/login")

    def username_input(self):
        self.driver.find_element(*self.USERNAME).send_keys('tomsmith')

    def password_input(self):
        self.driver.find_element(*self.PASSWORD).send_keys('SuperSecretPassword!')

    def enter_login_button(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()