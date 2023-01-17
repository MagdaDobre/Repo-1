from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class UserAccount(TestCase):
    ACCOUNT = (By.ID, 'ACCOUNT')
    CUSTOMER_LOGIN = (By.LINK_TEXT, 'Customer Login')

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("https://phptravels.net/")


    def tearDown(self):
        self.driver.quit()


    def test_Customer_Login(self):
        ACCOUNT = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.ID, 'ACCOUNT')))
        sleep(5)
        self.driver.find_element(By.ID, 'ACCOUNT').click()
        self.driver.find_element(By.LINK_TEXT, 'Customer Login').click()
        sleep(5)


    def test_url(self):
        exp_link = 'https://phptravels.net/login'
        actual_link = self.driver.current_url
        assert actual_link == exp_link, f'INVALID URL'

    def test_Tabs(self):
        ACCOUNT = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.ID, 'ACCOUNT')))
        sleep(5)

        # self.driver.find_element(By.LINK_TEXT, 'Hotels').click()
        # sleep(3)

        self.driver.find_element(By.LINK_TEXT, 'Flights').click()
        sleep(3)

        self.driver.find_element(By.NAME, "from").send_keys("Romania")
        sleep(3)

        self.driver.find_element(By.NAME, "to").send_keys("Spain")
        sleep(3)


