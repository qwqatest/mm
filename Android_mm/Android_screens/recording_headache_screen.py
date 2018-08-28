from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as ec
# Importing BaseScreen class
from .base_screen import *

# ------------------------------------------------------------------------------------------------------


class RecordingHeadache(BaseScreen):

    def click_earlier_today_button(self):
        # Click 'Earlier today' button
        earlier_today_button_location = (MobileBy.ID, 'com.migrainemonitor.dev:id/ll_earlier')
        earlier_today_button = WebDriverWait(self.driver, 20).until(
        ec.element_to_be_clickable(earlier_today_button_location))
        earlier_today_button.click()

    def click_just_now_button(self):
        # Click 'Just now' button
        just_now_button_location = (MobileBy.ID, 'com.migrainemonitor.dev:id/ll_now')
        just_now_button = WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable(just_now_button_location))
        just_now_button.click()

    def click_another_day_button(self):
        # Click 'Another day' button
        another_day_button_location = (MobileBy.ID, 'com.migrainemonitor.dev:id/ll_another')
        another_day_button = WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable(another_day_button_location))
        another_day_button.click()
        self.driver.back()