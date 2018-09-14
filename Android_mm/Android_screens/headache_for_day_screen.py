from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as ec
from appium import webdriver
# Importing BaseScreen class
from .base_screen import *
from time import sleep
from selenium.common.exceptions import NoSuchElementException
# ------------------------------------------------------------------------------------------------------


class BaseScreen(object):

    def __init__(self, driver):
        self.driver = driver


class HeadacheForADay(BaseScreen):

    def select_date_in_calendar(self):

        # date_location = (MobileBy.XPATH, '//TextView[contains(text(),"1")]')

        # Getting all dates in calendar as a list
        dates_location = (MobileBy.ID, 'com.migrainemonitor.dev:id/calendar_tv')
        dates = WebDriverWait(self.driver, 10).until(
            ec.presence_of_all_elements_located(dates_location))
        # dates[20].click()
        # sleep(2)

        # Select first available date without any headache recorded.
        # If "No headaches for current day" message is displayed, proceed to next step
        for date in dates:
            date.click()
            print(date.text)
            # sleep(0.5)
            try:
                self.driver.implicitly_wait(0)
                no_headaches_message = self.driver.find_element_by_android_uiautomator(
                    'new UiSelector().text("No headaches for current day")')
            except NoSuchElementException:
                    print('No headaches message')
            else:
                if no_headaches_message.is_displayed():
                    break

    def click_plus_button(self):

        plus_button_location = (MobileBy.ID, 'com.migrainemonitor.dev:id/fab_add_headache')
        plus_button = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(plus_button_location))
        plus_button.click()
