
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
        # tutorial_step.view_full_tutorial()
        # tutorial_step.home_screen_navigation_tutorial()
        # tutorial_step.entering_headache_tutorial()
        # tutorial_step.generating_report_tutorial()

        # Closing pop-up window

        tutorial_step.close_popup()

        # Entering Login and Password
        loggin_in_step = login_screen.LoginScreen(self.driver)
        # loggin_in_step.click_register_button()
        # loggin_in_step.click_facebook_login_button()
        # loggin_in_step.click_forgot_password_button()
        loggin_in_step.loggin_in('s.shtkov@gmail.com', 'qwerty12')

        # Allow access to the device location
        home = home_screen.HomeScreen(self.driver)
        home.allow_access()
        # home.click_hamburger_menu()
        # home.click_notes_button()
        # home.click_calendar_button()
        # home.click_migraine_news_button()
        # home.click_conversation_button()
        # home.click_provider_messages_button()
        # home.click_custom_pick_button()
        # home.set_current_stress_level()
        # home.clear_current_stress_level()

        # Click 'Record a Headache' button
        # home.click_record_headache_button()

        # Click 'Earlier today' button
        # recording_headache = recording_headache_screen.RecordingHeadache(self.driver)
        # recording_headache.click_earlier_today_button()

        # Click 'Just now' button
        # recording_headache.click_just_now_button()

        # Click 'Another day' button
        # recording_headache.click_another_day_button()

        # Click menu's buttons
        # home.click_report_menu_button()
        # home.click_community_menu_button()
        # home.click_provider_menu_button()
        home.click_profile_menu_button()

        my_profile = my_profile_screen.MyProfile(self.driver)
        # my_profile.changing_avatar_from_camera()
        # time.sleep(3)
        # my_profile.changing_avatar_from_library()
        # time.sleep(3)
        # my_profile.set_next_appointment_date()
        # time.sleep(3)
        my_profile.switch_daily_notification()
        my_profile.set_date_of_birth()
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()