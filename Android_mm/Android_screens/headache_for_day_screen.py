from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as ec
# Importing BaseScreen class
from .base_screen import *

# ------------------------------------------------------------------------------------------------------


class HeadacheForADay(BaseScreen):

    def select_date_in_calendar(self):

        date_location = (MobileBy.CLASS_NAME, 'android.widget.TextView')
        date = WebDriverWait(self.driver, 10).until(
            ec.presence_of_all_elements_located(date_location))
        date[22].click()

    def click_plus_button(self):

        plus_button_location = (MobileBy.ID, 'com.migrainemonitor.dev:id/fab_add_headache')
        plus_button = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(plus_button_location))
        plus_button.click()
