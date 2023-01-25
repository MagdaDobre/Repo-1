from browser import Browser
from selenium.webdriver.common.by import By

class Secure_Page(Browser):
    MESSAGE_SUCCES_LOGIN = (By.ID, "flash")
    LOGOUT_BTN = (By.XPATH, "//*[contains(text(), 'Logout')]")


    def navigate_to_secure_page(self):
        self.driver.get("https://the-internet.herokuapp.com/secure")

    def check_message_succes__is_displayed(self):
        actual = self.driver.find_element(*self.MESSAGE_SUCCES_LOGIN).text
        expected = ' You logged into a secure area!'
        assert actual == expected, f"The success message is NOT displayed!"

    def logout_btn(self):
        self.driver.find_element(*self.LOGOUT_BTN).click()



