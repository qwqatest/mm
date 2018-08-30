
import unittest
from appium import webdriver

# from Android_mm.Android_screens import tutorial_screen, login_screen, home_screen, recording_headache_screen
from Android_mm.Android_screens import *
import time


# _________________________________________________________________________________________________________________

class TestMM(unittest.TestCase):

    def setUp(self):

        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '8.1'
        desired_caps['deviceName'] = 'Android'
        desired_caps['app'] = '/Users/sergey/Desktop/mmonitor-dev.apk'
        desired_caps['appPackage'] = 'com.migrainemonitor.dev'
        desired_caps['appActivity'] = 'com.migrainemonitor.ui.activity.SplashActivity'
        desired_caps['cleaning'] = 'clearSystemFiles'
        desired_caps['automationName'] = 'UiAutomator2'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(20)

    def test_some_flow(self):

        tutorial_step = tutorial_screen.TutorialScreen(self.driver)

        # Closing pop-up window
        tutorial_step.close_popup()

        # Entering Login and Password
        loggin_in_step = login_screen.LoginScreen(self.driver)
        loggin_in_step.loggin_in('qwqatest@gmail.com', 'qwerty12')

        # Allow access to the device location
        home = home_screen.HomeScreen(self.driver)
        home.allow_access()

        home.click_hamburger_menu()
        time.sleep(1)
        self.driver.back()

        home.click_notes_button()
        time.sleep(1)
        self.driver.back()

        home.click_calendar_button()
        time.sleep(2)
        self.driver.back()

        home.click_migraine_news_button()
        time.sleep(3)
        self.driver.back()

        home.click_conversation_button()
        time.sleep(2)
        self.driver.back()
        self.driver.back()

        home.click_provider_messages_button()
        time.sleep(1)
        self.driver.back()

        home.click_custom_pick_button()
        time.sleep(1)
        self.driver.back()

        home.set_current_stress_level()
        time.sleep(4)
        home.clear_current_stress_level()
        time.sleep(3)

        # Click 'Record a Headache' button
        home.click_record_headache_button()

        # Click 'Earlier today' button
        recording_headache = recording_headache_screen.RecordingHeadache(self.driver)
        recording_headache.click_earlier_today_button()

        # Click 'Just now' button
        recording_headache.click_just_now_button()

        # Click 'Another day' button
        recording_headache.click_another_day_button()
        self.driver.back()

        # Click base menu's buttons
        home.click_report_menu_button()
        time.sleep(1)
        self.driver.back()

        home.click_community_menu_button()
        time.sleep(1)
        self.driver.back()

        home.click_provider_menu_button()
        time.sleep(1)
        self.driver.back()

        home.click_profile_menu_button()

    def tearDown(self):
       self.driver.quit()


if __name__ == '__main__':
    unittest.main()