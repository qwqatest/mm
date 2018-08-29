
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as ec
# Importing BaseScreen class
from .base_screen import *
import time

# ------------------------------------------------------------------------------------------------------


class LoginScreen(BaseScreen):

    def loggin_in(self, login, password):

        # Entering Login and Password
        login_location = (MobileBy.ID, 'com.migrainemonitor.dev:id/edit_email')
        login_input = WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable(login_location))
        login_input.send_keys(login)

        password_location = (MobileBy.ID, 'com.migrainemonitor.dev:id/edit_password')
        password_input = WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable(password_location))
        password_input.send_keys(password)

        #Hiding keyboard
        # self.driver.hide_keyboard()

        # Clicking on the login button
        login_button = self.driver.find_element_by_id('com.migrainemonitor.dev:id/btn_login')
        login_button.click()

    def click_register_button(self):
        register_button_location = (MobileBy.ID, 'com.migrainemonitor.dev:id/btn_registration')
        register_button = WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable(register_button_location))
        register_button.click()

    def click_facebook_login_button(self):
        facebook_login_button_location = (MobileBy.ID, 'com.migrainemonitor.dev:id/btn_facebook_login')
        facebook_login_button = WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable(facebook_login_button_location))
        facebook_login_button.click()

    def click_forgot_password_button(self):
        forgot_password_button_location = (MobileBy.ID, 'com.migrainemonitor.dev:id/tv_forgot_password')
        forgot_password_button = WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable(forgot_password_button_location))
        forgot_password_button.click()