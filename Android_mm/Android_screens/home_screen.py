
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as ec
# Importing BaseScreen class
from .base_screen import *
from appium.webdriver.common.touch_action import TouchAction
import time

# ------------------------------------------------------------------------------------------------------


class HomeScreen(BaseScreen):

    def allow_access(self):

        allow_button_location = (MobileBy.ID, 'com.android.packageinstaller:id/permission_allow_button')
        allow_button = WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable(allow_button_location))
        allow_button.click()

    def click_hamburger_menu(self):

        hamburger_menu_button_location = (MobileBy.ACCESSIBILITY_ID, 'open navigation drawer')
        hamburger_menu_button = WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable(hamburger_menu_button_location))
        hamburger_menu_button.click()
        time.sleep(1)
        self.driver.back()

    def click_notes_button(self):

        notes_button_location = (MobileBy.ACCESSIBILITY_ID, 'Notes')
        notes_button = WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable(notes_button_location))
        notes_button.click()
        time.sleep(1)
        self.driver.back()

    def click_calendar_button(self):

        calendar_button_location = (MobileBy.ACCESSIBILITY_ID, 'Calendar')
        calendar_button = WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable(calendar_button_location))
        calendar_button.click()
        time.sleep(2)
        self.driver.back()

    def click_migraine_news_button(self):
        # Waiting when Calendar button will be on the screen to be sure we've returned to the Home screen
        calendar_button_location = (MobileBy.ACCESSIBILITY_ID, 'Calendar')
        WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable(calendar_button_location))
        TouchAction(self.driver).tap(None, 471, 1311, 1).perform()
        # news_title_location = self.driver.('text("News")')
        # WebDriverWait(self.driver, 20).until(ec.presence_of_element_located(news_title_location))
        time.sleep(2)
        self.driver.back()

    def click_conversation_button(self):
        conversation_button_location = (MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.TextView')
        conversation_button = WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable(conversation_button_location))
        conversation_button.click()
        time.sleep(1)
        self.driver.back()
        self.driver.back()

    def click_provider_messages_button(self):
        provider_messages_button_location = (MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.TextView')
        provider_messages_button = WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable(provider_messages_button_location))
        provider_messages_button.click()
        time.sleep(1)
        self.driver.back()

    def click_custom_pick_button(self):
        custom_pick_button_location = (MobileBy.ID, 'com.migrainemonitor.dev:id/tv_custom_pick')
        custom_pick_button = WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable(custom_pick_button_location))
        custom_pick_button.click()
        time.sleep(1)
        self.driver.back()

    def click_report_menu_button(self):
        # Click report menu button
        report_menu_button_location = (MobileBy.ID, 'com.migrainemonitor.dev:id/base_menu_report')
        report_menu_button = WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable(report_menu_button_location))
        report_menu_button.click()

    def click_record_headache_button(self):
        # Click 'Record a Headache' button
        record_button_location = (MobileBy.ID, 'com.migrainemonitor.dev:id/fl_circle')
        record_button = WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable(record_button_location))
        record_button.click()