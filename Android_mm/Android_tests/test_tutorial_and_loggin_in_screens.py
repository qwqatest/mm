import unittest
from appium import webdriver

# from Android_mm.Android_screens import tutorial_screen, login_screen, home_screen, recording_headache_screen
from Android_mm.Android_screens import *
import time


# _________________________________________________________________________________________________________________

class TestTutorialAndLoggin(unittest.TestCase):

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

    def test_tutorial_loggin_in_screens(self):
        
        # Clicking all buttons on this screen
        tutorial_step = tutorial_screen.TutorialScreen(self.driver)
        tutorial_step.view_full_tutorial()
        time.sleep(1)
        self.driver.back()

        tutorial_step.home_screen_navigation_tutorial()
        time.sleep(1)
        self.driver.back()

        tutorial_step.entering_headache_tutorial()
        time.sleep(1)
        self.driver.back()

        tutorial_step.generating_report_tutorial()
        time.sleep(1)
        self.driver.back()

        # Closing pop-up window
        tutorial_step.close_popup()

        # Clicking all buttons on this screen
        loggin_in_step = login_screen.LoginScreen(self.driver)
        loggin_in_step.click_register_button()
        time.sleep(1)
        self.driver.back()

        loggin_in_step.click_facebook_login_button()
        time.sleep(3)
        self.driver.back()

        loggin_in_step.click_forgot_password_button()
        time.sleep(1)
        self.driver.back()
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
