
import unittest
from appium import webdriver

# from Android_mm.Android_screens import tutorial_screen, login_screen, home_screen, recording_headache_screen
from Android_mm.Android_screens import *
import time

# _________________________________________________________________________________________________________________


class TestFullFlow(unittest.TestCase):

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
        self.email = ("qwqatest+%i@gmail.com" % (time.time()))

    def test_full_flow(self):

        self.driver.implicitly_wait(20)
        # Closing pop-up window
        tutorial_step = tutorial_screen.TutorialScreen(self.driver)
        tutorial_step.close_popup()

        # Entering Login and Password
        loggin_in_step = login_screen.LoginScreen(self.driver)
        loggin_in_step.click_register_button()

        registration_step = registration_screen.RegistrationScreen(self.driver)
        registration_step.new_user_registration(self.email, 'Qw', 'Qw', 'qwerty12', 'qwerty12')
        registration_step.click_get_started_button()

        # Allow access to the device location
        home = home_screen.HomeScreen(self.driver)
        home.allow_access()

        # Click 'Record a Headache' button
        # home.click_record_headache_button()
        home.click_calendar_button()
        time.sleep(2)
        headache_for_day = headache_for_day_screen.HeadacheForADay(self.driver)
        headache_for_day.select_date_in_calendar()
        headache_for_day.click_plus_button()

        # Click 'Another day' button
        recording_headache = recording_headache_screen.RecordingHeadache(self.driver)
        # recording_headache.click_another_day_button()

        # recording_headache.move_days_picker_on_yesterday()
        recording_headache.click_ok_next_button()
        recording_headache.click_no_button()

        recording_headache.move_days_picker_on_today()
        recording_headache.click_ok_next_button()

        #  _________________________________  "How did you feel?" step  ________________________________
        recording_headache.set_headache_pain_intensity()
        recording_headache.set_stress_level_before_headache()
        recording_headache.select_aura_with_headache()
        recording_headache.select_speech_difficulty_checkbox()
        recording_headache.select_visual_checkbox()
        recording_headache.select_weakness_checkbox()
        recording_headache.click_ok_next_button()

        #   ___________________________  "Pain location" step   _________________________________________
        recording_headache.select_temporal_right_dot()
        recording_headache.select_upper_nape_left_dot()
        recording_headache.click_ok_next_button()

        #   ___________________________  "Possible triggers" step   _____________________________________
        recording_headache.select_stress_trigger_checkbox()
        recording_headache.select_little_sleep_trigger_checkbox()
        recording_headache.click_skip_next_button()

        #   ___________________________  "Note & Other symptoms" step   __________________________________
        recording_headache.make_a_note('This message was created by Appium')
        recording_headache.select_dizziness_checkbox()
        recording_headache.select_light_sensitivity_checkbox()
        recording_headache.select_nausea_checkbox()
        recording_headache.select_vomiting_checkbox()
        recording_headache.click_skip_next_button()

        #   ___________________________  "Your headache summary" step   __________________________________
        recording_headache.click_submit_button()
        #   ___________________________  "Medications" step   __________________________________
        recording_headache.click_done_button()

        recording_headache.click_done_button()

        time.sleep(5)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
