from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as ec

# Importing BaseScreen class
from .base_screen import *
import time

# _________________________________________________________________________________________________________________


class RegistrationScreen(BaseScreen):

    def new_user_registration(self, email, first_name, last_name, password, password2):

        # Enter email address
        email_field_location = (MobileBy.ID, 'com.migrainemonitor.dev:id/edit_email')
        email_field = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(email_field_location))
        email_field.send_keys(email)
        # time.sleep(1)

        # Enter First name
        first_name_field_location = (MobileBy.ID, 'com.migrainemonitor.dev:id/edit_first_name')
        first_name_field = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(first_name_field_location))
        first_name_field.send_keys(first_name)
        # time.sleep(1)

        # Enter Last name
        last_name_field_location = (MobileBy.ID, 'com.migrainemonitor.dev:id/edit_last_name')
        last_name_field = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(last_name_field_location))
        last_name_field.send_keys(last_name)
        # time.sleep(1)

        # Click Birth date button
        birth_date_button_location = (MobileBy.ID, 'com.migrainemonitor.dev:id/btn_birth_date')
        birth_date_button = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(birth_date_button_location))
        birth_date_button.click()

        # Click 'Ok'button
        ok_button_location = (MobileBy.ID, 'android:id/button1')
        ok_button = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(ok_button_location))
        ok_button.click()

        # Set password
        password_field_location = (MobileBy.ID, 'com.migrainemonitor.dev:id/edit_password')
        password_field = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(password_field_location))
        password_field.send_keys(password)

        # Repeat password
        password2_field_location = (MobileBy.ID, 'com.migrainemonitor.dev:id/edit_password_repeat')
        password2_field = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(password2_field_location))
        password2_field.send_keys(password2)

        # Click Register button
        register_button_location = (MobileBy.ID, 'com.migrainemonitor.dev:id/btn_register')
        register_button = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(register_button_location))
        register_button.click()
        time.sleep(2)

        # Click 'Don't have a provider' button
        no_provider_button_location = (MobileBy.ID, 'com.migrainemonitor.dev:id/btn_dont_have_doctor')
        no_provider_button = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(no_provider_button_location))
        no_provider_button.click()
        time.sleep(1)

    def click_get_started_button(self):
        get_started_button_location = (MobileBy.ID, 'com.migrainemonitor.dev:id/btn_get_started')
        get_started_button = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(get_started_button_location))
        get_started_button.click()
