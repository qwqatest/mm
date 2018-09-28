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
        # time.sleep(2)

        # Click 'Don't have a provider' button
        # no_provider_button_location = (MobileBy.ID, 'com.migrainemonitor.dev:id/btn_dont_have_doctor')
        # no_provider_button = WebDriverWait(self.driver, 20).until(
        #     ec.element_to_be_clickable(no_provider_button_location))
        # no_provider_button.click()
        # time.sleep(1)

        # Search for your Provider
        search_field_location = (MobileBy.ID, 'com.migrainemonitor.dev:id/edit_search')
        search_field = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(search_field_location))
        search_field.send_keys("qw ")
        # time.sleep(1)

        # Select first name from the search list
        doctor_name_location = (MobileBy.ID, 'com.migrainemonitor.dev:id/tv_doctor_name')
        doctor_name = WebDriverWait(self.driver, 10).until(
            ec.presence_of_all_elements_located(doctor_name_location))
        doctor_name[0].click()

        # Click 'Done' button
        done_button_location = (MobileBy.ID, 'com.migrainemonitor.dev:id/btn_done')
        done_button = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(done_button_location))
        done_button.click()

        # Select How did you hear of us option
        checkboxes_location = (MobileBy.CLASS_NAME, 'android.widget.CheckBox')
        checkboxes = WebDriverWait(self.driver, 10).until(
            ec.presence_of_all_elements_located(checkboxes_location))
        checkboxes[3].click()

        # Click 'Next' button
        next_button_location = (MobileBy.ID, 'com.migrainemonitor.dev:id/btn_next')
        next_button = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(next_button_location))
        next_button.click()

    def click_get_started_button(self):
        get_started_button_location = (MobileBy.ID, 'com.migrainemonitor.dev:id/btn_get_started')
        get_started_button = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(get_started_button_location))
        get_started_button.click()


# el1 = driver.find_element_by_id("com.migrainemonitor.dev:id/edit_search")
# el1.send_keys("qw ")
# el2 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]")
# el2.click()
# el3 = driver.find_element_by_id("com.migrainemonitor.dev:id/btn_done")
# el3.click()
# el4 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.view.ViewGroup[4]/android.widget.CheckBox")
# el4.click()
# el5 = driver.find_element_by_id("com.migrainemonitor.dev:id/btn_next")
# el5.click()
# el6 = driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
# el6.click()
# el7 = driver.find_element_by_id("android:id/button1")
# el7.click()