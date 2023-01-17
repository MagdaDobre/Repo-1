import unittest
from unittest import TestCase
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class Login(unittest.TestCase):
    Form_Authentication = (By.LINK_TEXT, "Form Authentication")
    Login_page = (By.XPATH, '//h2[text() = "Login Page"]')
    LOGIN_BUTTON =(By.XPATH, "//i[@class = 'fa fa-2x fa-sign-in']")
    Atribut_Elemental_Selenium = (By.LINK_TEXT, "Elemental Selenium")
    Login_error = (By.ID, "flash")
    Username = (By.ID, "username")
    Password = (By.ID, "password")
    Error_closed = (By.XPATH, '//a[@class = "close"]')
    Label = (By.TAG_NAME, "label")
    Flash_class = (By.ID, "flash")
    Logout = (By.XPATH, "//i[contains(text(),'Logout')]")
    Subheader = (By.XPATH, '//h4')

    def setUp(self):
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(10)
        self.chrome.get("https://the-internet.herokuapp.com/")
        self.chrome.find_element(*self.Form_Authentication).click()

    def tearDown(self):
        self.chrome.quit()

    # Test 1 - Verifică dacă noul url e corect
    def test_url(self):
        actual_url = self.chrome.current_url
        expected_url = "https://the-internet.herokuapp.com/login"
        self.assertEqual(actual_url, expected_url, "Url este incorect")

    # Test 2 - Verifică dacă page title e corect
    def test_page_title(self):
        actual_title = self.chrome.title
        expected_title = "The Internet"
        self.assertEqual(actual_title, expected_title, "Title incorrect")

    # Test 3 - Verifică textul de pe elementul xpath=//h2 e corect
    def test_Login_page(self):
        actual_text = self.chrome.find_element(*self.Login_page).text
        expected_text = "Login Page"
        self.assertEqual(actual_text, expected_text, "Text incorrect")

    # Test 4 - Verifică dacă butonul de login este displayed
    def test_button_login_displayed(self):
        btn = self.chrome.find_element(*self.LOGIN_BUTTON)
        self.assertTrue(btn.is_displayed(), 'Butonul nu este displayed')

    # Test 5 - Verifică dacă atributul href al linkului ‘Elemental Selenium’ e corect
    def test_href(self):
        actual = self.chrome.find_element(*self.Atribut_Elemental_Selenium).get_attribute('href')
        expected = 'http://elementalselenium.com/'
        self.assertEqual(actual, expected, 'The attribute value is not correct')

    # Test 6
    # - Lasă goale user și pass
    # - Click login
    # - Verifică dacă eroarea e displayed
    def test_Login_error_displayed(self):
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        error = self.chrome.find_element(*self.Login_error)
        self.assertTrue(error.is_displayed(), 'Eroarea nu este afisata')

    # Test 7
    # - Completează cu user și pass invalide
    # - Click login
    # - Verifică dacă mesajul de pe eroare e corect
    # - Este și un x pus acolo extra așa că vom folosi soluția de mai jos
    # expected = 'Your username is invalid!'
    # self.assertTrue(expected in actual, 'Error message text is incorrect')

    def test_error_message_correct(self):
        self.chrome.find_element(*self.Username).send_keys("test123")
        self.chrome.find_element(*self.Password).send_keys("pass1234")
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        actual = self.chrome.find_element(*self.Login_error).text
        expected = 'Your username is invalid!'
        self.assertTrue(expected in actual, 'Error message text is incorrect')

    # Test 8
    # - Lasă goale user și pass
    # - Click login
    # - Apasă x la eroare
    # - Verifică dacă eroarea a dispărut

    def test_error_closed(self):
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        self.chrome.find_element(*self.Error_closed).click()
        sleep(3)
        try:
            self.chrome.find_element(*self.Error_closed)
        except NoSuchElementException:
            print("Eroarea nu este afisata, e ok")

    # Test 9
    # - Ia ca o listă toate //label
    # - Verifică textul ca textul de pe ele să fie cel așteptat (Username și Password)
    # - Aici e ok să avem 2 asserturi

    def test_label(self):
        label = self.chrome.find_elements(*self.Label)
        print(f'Lista returnata este {len(label)}')
        expected_text = ['Username', 'Password']
        self.assertEqual(label[0].text, expected_text[0], f"Label text is {label}, and expected text was {expected_text}.")
        self.assertEqual(label[1].text, expected_text[1], f"Label text is {label}, and expected text was {expected_text}.")

    # ● Test 10
    # - Completează cu user și pass valide
    # - Click login
    # - Verifică ca noul url CONTINE /secure
    # - Folosește un explicit wait pentru elementul cu clasa ’flash succes’
    # - Verifică dacă elementul cu clasa=’flash succes’ este displayed
    # - Verifică dacă mesajul de pe acest element CONȚINE textul ‘secure area!’

    def test_nou_url(self):
        self.chrome.find_element(*self.Username).send_keys("tomsmith")
        self.chrome.find_element(*self.Password).send_keys("SuperSecretPassword!")
        self.chrome.find_element(*self.LOGIN_BUTTON).click()

        WebDriverWait(self.chrome, 5).until(EC.url_contains('/secure'))
        WebDriverWait(self.chrome, 5).until(EC.url_to_be('https://the-internet.herokuapp.com/secure'))

        flash_cls = WebDriverWait(self.chrome, 15).until(EC.presence_of_element_located((By.ID, "flash")))
        self.assertTrue(flash_cls.is_displayed(), 'Clasa=’flash succes’ nu este displayed')

        actual = self.chrome.find_element(*self.Flash_class).text
        expected = "secure area!"
        self.assertTrue(expected in actual, "Text expected is not in the actual form.")

    # Test 11
    # - Completează cu user și pass valide
    # - Click login
    # - Click logout
    # - Verifică dacă ai ajuns pe https://the-internet.herokuapp.com/login

    def test_url_login(self):
        self.chrome.find_element(*self.Username).send_keys("tomsmith")
        self.chrome.find_element(*self.Password).send_keys("SuperSecretPassword!")
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        self.chrome.find_element(*self.Logout).click()

        WebDriverWait(self.chrome, 5).until(EC.url_contains('/login'))
        WebDriverWait(self.chrome, 5).until(EC.url_to_be('https://the-internet.herokuapp.com/login'))

    # Test 12 - brute force password hacking
    # - Completează user tomsmith
    # - Găsește elementul //h4
    # - Ia textul de pe el și fă split după spațiu. Consideră fiecare cuvânt ca o potențială parolă.
    # - Folosește o structură iterativă prin care să introduci rând pe rând parolele și să apeși pe login.
    # - La final testul trebuie să îmi printeze fie
    # ‘Nu am reușit să găsesc parola’
    # ‘Parola secretă este [parola]’

    def test_brute_force_password_hacking(self):
        h4_text = self.chrome.find_element(*self.Subheader).text
        possible_password = h4_text.split()
        print(possible_password)

        for password in possible_password:
            self.chrome.find_element(*self.Username).send_keys("tomsmith")
            self.chrome.find_element(*self.Password).send_keys(password)
            self.chrome.find_element(*self.LOGIN_BUTTON).click()

            actual_url = self.chrome.current_url
            expected_url = "https://the-internet.herokuapp.com/secure"

            if actual_url == expected_url:
                print(f"Parola secreta este {password}")
                break
            else:
                print("Nu am reusit sa gasesc parola")

