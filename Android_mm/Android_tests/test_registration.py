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
        self.email = ("qwqatest+%i@gmail.com" % (time.time()))

    def test_registration(self):

        # Closing pop-up window
        tutorial_step = tutorial_screen.TutorialScreen(self.driver)
        tutorial_step.close_popup()

        # Entering Login and Password
        loggin_in_step = login_screen.LoginScreen(self.driver)
        loggin_in_step.click_register_button()

        registration_step = registration_screen.RegistrationScreen(self.driver)
        registration_step.new_user_registration(self.email, 'Qw', 'Qw', 'qwerty12', 'qwerty12')

        my_profile = my_profile_screen.MyProfile(self.driver)
        my_profile.assert_user_name()

        time.sleep(3)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
