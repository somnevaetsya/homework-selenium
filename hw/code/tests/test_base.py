from pageobjects.pages.base import BasePage
from pageobjects.components.header import Header
from pageobjects.components.modal_desk import ModalDesk
from tests.base_test_case import BaseTestCase
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utils.constants import authorization_data,urls,cookie_name,create_desc_errors

class BaseTest(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.page = BasePage(self.driver)

    def sign_up(self):
        self.signUpPage.open()
        self.signUpPage.signup_new_user()
        Header.create(self.driver)

    def sign_up_create_desk(self, title, desc):
        self.sign_up()
        self.page.create_desk(title, desc)

    def test_create_desk_without_desc(self):  # Найденов Александр Валентинович
        title = "title"
        desc = ""
        self.sign_up_create_desk(title, desc)
        self.assertEqual(self.page.check_new_desk(title, desc), True)

    def test_create_desk_with_desc(self):  # Найденов Александр Валентинович
        title = "title"
        desc = "desctiption"
        self.sign_up_create_desk(title, desc)
        self.assertEqual(self.page.check_new_desk(title, desc), True)

    def test_close_popup_icon(self): # Иванов Виктор Михайлович
        self.sign_up()
        self.page.btn_new_desk.click()
        ModalDesk.create(self.driver)
        self.page.popup_icon_close
        self.assertEqual(self.page.popup_new_desk_check_active, False)
    
    def test_close_popup_btn(self): # Иванов Виктор Михайлович
        self.sign_up()
        self.page.btn_new_desk.click()
        ModalDesk.create(self.driver)
        self.page.popup_btn_close
        self.assertEqual(self.page.popup_new_desk_check_active, False)

    def test_short_title(self): # Найденов Александр Валентинович
        title = ""
        desc = ""
        self.sign_up_create_desk(title, desc)
        self.assertEqual(self.page.get_error(), create_desc_errors["invalid_title"])
    
    def test_long_title(self): # Найденов Александр Валентинович
        title = "awdkoawopdkopawdkopawkdawkpdkaowdkopawkdpawod"
        desc = ""
        self.sign_up_create_desk(title, desc)
        self.assertEqual(self.page.get_error(), create_desc_errors["invalid_title"])


    
