from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as ec
# Importing BaseScreen class
from .base_screen import *
from appium.webdriver.common.touch_action import TouchAction
import time

# _________________________________________________________________________________________________________________


class MyProfile(BaseScreen):

    def changing_avatar_from_camera(self):

        # Click on the user avatar
        avatar_location = (MobileBy.ID, 'com.migrainemonitor.dev:id/iv_user_avatar')
        avatar = WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable(avatar_location))
        avatar.click()
        # time.sleep(1)

        # Select source from where picture will be taken
        camera_button_location = (MobileBy.ID, 'com.migrainemonitor.dev:id/button_camera_photo')
        select_camera_button = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(camera_button_location))
        select_camera_button.click()
        # time.sleep(1)

        # Allow camera use
        allow_camera_button_location = (MobileBy.ID, 'com.android.packageinstaller:id/permission_allow_button')
        allow_camera_button = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(allow_camera_button_location))
        allow_camera_button.click()
        time.sleep(1)
        allow_camera_button.click()
        time.sleep(2)

        # Click Shutter button
        shutter_button_location = (MobileBy.ACCESSIBILITY_ID, 'Shutter')
        shutter_button = WebDriverWait(self.driver, 20).until(
            ec.visibility_of_element_located(shutter_button_location))
        shutter_button.click()
        time.sleep(4)

        # Click Done button
        done_button_location = (MobileBy.ACCESSIBILITY_ID, 'Done')
        done_button = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(done_button_location))
        done_button.click()
        # time.sleep(3)

        # Click Crop button
        crop_button_location = (MobileBy.ID, 'com.migrainemonitor.dev:id/crop_image_menu_crop')
        crop_button = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(crop_button_location))
        crop_button.click()
        time.sleep(1)

    def changing_avatar_from_library(self):

        # Click on the user avatar
        avatar_location = (MobileBy.ID, 'com.migrainemonitor.dev:id/iv_user_avatar')
        avatar = WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable(avatar_location))
        avatar.click()
        # time.sleep(1)

        # Select source from where picture will be taken
        library_button_location = (MobileBy.ID, 'com.migrainemonitor.dev:id/button_library_photo')
        select_library_button = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(library_button_location))
        select_library_button.click()
        # time.sleep(1)

        # Allow library use
        # allow_library_button_location = (MobileBy.ID, 'com.android.packageinstaller:id/permission_allow_button')
        # allow_library_button = WebDriverWait(self.driver, 20).until(
        #     ec.element_to_be_clickable(allow_library_button_location))
        # allow_library_button.click()
        # time.sleep(1)

        # Select Photos folder
        photos_folder_location = (MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.ImageView')
        photos_folder = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(photos_folder_location))
        photos_folder.click()
        # time.sleep(3)

        # Select a photo
        photo_location = (MobileBy.ACCESSIBILITY_ID,'Photo taken on Aug 15, 2017 18:48:41')
        photo = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(photo_location))
        photo.click()
        # time.sleep(3)

        # Click Crop button
        crop_button_location = (MobileBy.ID, 'com.migrainemonitor.dev:id/crop_image_menu_crop')
        crop_button = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(crop_button_location))
        crop_button.click()

    def set_next_appointment_date(self):

        # Click on next appointment link
        next_appointment_location = (MobileBy.ID, 'com.migrainemonitor.dev:id/tv_appointment_date')
        next_appointment = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(next_appointment_location))
        next_appointment.click()

        # Click next day 7 times
        next_day_location = (MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.DatePicker/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.NumberPicker[2]/android.widget.Button[2]')
        next_day = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(next_day_location))
        next_day.click()

        # Click 'Ok'button
        ok_button_location = (MobileBy.ID, 'android:id/button1')
        ok_button = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(ok_button_location))
        ok_button.click()

    def set_date_of_birth(self):

        # Click on the birth date link
        date_of_birth_link_location = (MobileBy.ID, 'com.migrainemonitor.dev:id/tv_date_of_birth')
        date_of_birth_link = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(date_of_birth_link_location))
        date_of_birth_link.click()

        # Set new birth date
        previous_day_location = (MobileBy.XPATH,
                             '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.DatePicker/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.NumberPicker[2]/android.widget.Button[1]')
        previous_day = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(previous_day_location))
        previous_day.click()

        # Click 'Ok'button
        ok_button_location = (MobileBy.ID, 'android:id/button1')
        ok_button = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(ok_button_location))
        ok_button.click()

    def switch_daily_notification(self):

        remind_switcher_location = (MobileBy.ID, 'com.migrainemonitor.dev:id/switch_daily_notification')
        remind_switcher = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(remind_switcher_location))
        remind_switcher.click()

    def assert_user_name(self):
        # Checking user name
        user_name_location = (MobileBy.ID, 'com.migrainemonitor.dev:id/tv_user_username')
        user_name = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(user_name_location))
        assert user_name.text == 'Qw Qw'
        print(user_name.text)
        time.sleep(1)

