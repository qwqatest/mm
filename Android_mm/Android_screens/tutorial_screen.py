
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as ec

# Importing BaseScreen class
from .base_screen import *
import time

# ------------------------------------------------------------------------------------------------------


class TutorialScreen(BaseScreen):

    def view_full_tutorial(self):
        view_full_tutorial_button_location = (MobileBy.ID, 'com.migrainemonitor.dev:id/btn_full_tutorial')
        view_full_tutorial_button = WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable(view_full_tutorial_button_location))
        view_full_tutorial_button.click()
        time.sleep(1)
        self.driver.back()

    def home_screen_navigation_tutorial(self):
        home_screen_navigation_tutorial_button_location = (MobileBy.ID, 'com.migrainemonitor.dev:id/btn_home_tutorial')
        home_screen_navigation_tutorial_button = WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable(home_screen_navigation_tutorial_button_location))
        home_screen_navigation_tutorial_button.click()
        time.sleep(1)
        self.driver.back()

    def entering_headache_tutorial(self):
        entering_headache_tutorial_button_location = (MobileBy.ID, 'com.migrainemonitor.dev:id/btn_headache_tutorial')
        entering_headache_tutorial_button = WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable(entering_headache_tutorial_button_location))
        entering_headache_tutorial_button.click()
        time.sleep(1)
        self.driver.back()

    def generating_report_tutorial(self):
        generating_report_tutorial_button_location = (MobileBy.ID, 'com.migrainemonitor.dev:id/btn_reports_tutorial')
        generating_report_tutorial_button = WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable(generating_report_tutorial_button_location))
        generating_report_tutorial_button.click()
        time.sleep(1)
        self.driver.back()

    def close_popup(self):

        # Closing pop-up window
        close_button_location = (MobileBy.ID, 'com.migrainemonitor.dev:id/iv_close')
        close_button = WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable(close_button_location))
        close_button.click()