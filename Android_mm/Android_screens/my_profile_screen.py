from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as ec
# Importing BaseScreen class
from .base_screen import *
from appium.webdriver.common.touch_action import TouchAction
import time


class MyProfile(BaseScreen):

    def changing_avatar_from_camera(self):

        # Click on the  user avatar
        avatar_location = (MobileBy.ID, 'com.migrainemonitor.dev:id/iv_user_avatar')
        avatar = WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable(avatar_location))
        avatar.click()
        time.sleep(1)

        # Select source from where picture will be taken
        select_camera_button_location = (MobileBy.ID, 'com.migrainemonitor.dev:id/button_camera_photo')
        select_camera_button = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(select_camera_button_location))
        select_camera_button.click()
        time.sleep(1)

        # Allow camera use
        allow_camera_button_location = (MobileBy.ID, 'com.android.packageinstaller:id/permission_allow_button')
        allow_camera_button = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(allow_camera_button_location))
        allow_camera_button.click()
        time.sleep(1)
        allow_camera_button.click()
        time.sleep(1)

        # Click Shutter button
        shutter_button_location = (MobileBy.ACCESSIBILITY_ID, 'Shutter')
        shutter_button = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(shutter_button_location))
        shutter_button.click()
        time.sleep(3)

        # Click Done button
        done_button_location = (MobileBy.ACCESSIBILITY_ID, 'Done')
        done_button = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(done_button_location))
        done_button.click()
        time.sleep(3)

        # Click Crop button
        crope_button_location = (MobileBy.ID, 'com.migrainemonitor.dev:id/crop_image_menu_crop')
        crope_button = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(crope_button_location))
        crope_button.click()
        time.sleep(1)
