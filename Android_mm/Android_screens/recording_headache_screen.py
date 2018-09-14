from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as ec
# Importing BaseScreen class
from .base_screen import *
# from selenium.webdriver.common.touch_actions import TouchActions
from appium.webdriver.common.touch_action import TouchAction
# ------------------------------------------------------------------------------------------------------


class RecordingHeadache(BaseScreen):

    def click_earlier_today_button(self):
        # Click 'Earlier today' button
        earlier_today_button_location = (MobileBy.ID, 'com.migrainemonitor.dev:id/ll_earlier')
        earlier_today_button = WebDriverWait(self.driver, 20).until(
        ec.element_to_be_clickable(earlier_today_button_location))
        earlier_today_button.click()

    def click_just_now_button(self):
        # Click 'Just now' button
        just_now_button_location = (MobileBy.ID, 'com.migrainemonitor.dev:id/ll_now')
        just_now_button = WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable(just_now_button_location))
        just_now_button.click()

    def click_another_day_button(self):
        # Click 'Another day' button
        another_day_button_location = (MobileBy.ID, 'com.migrainemonitor.dev:id/ll_another')
        another_day_button = WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable(another_day_button_location))
        another_day_button.click()

    def move_days_picker_on_yesterday(self):
        days_picker_location = (MobileBy.ID, 'com.migrainemonitor.dev:id/ll_another')
        WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(days_picker_location))
        TouchAction(self.driver).press(x=445, y=902).move_to(x=453, y=1065).release().perform()

    def click_ok_next_button(self):

        # Click 'Ok' button
        ok_next_button_location = (MobileBy.ID, 'com.migrainemonitor.dev:id/btn_next')
        ok_next_button = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(ok_next_button_location))
        ok_next_button.click()

    def click_no_button(self):

        # Click 'Ok' button
        no_button_location = (MobileBy.ID, 'com.migrainemonitor.dev:id/btn_no')
        no_button = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(no_button_location))
        no_button.click()

    def move_days_picker_on_today(self):

        days_picker_location = (MobileBy.ID, 'com.migrainemonitor.dev:id/ll_another')
        WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(days_picker_location))
        TouchAction(self.driver).press(x=468, y=1201).move_to(x=468, y=1123).release().perform()

    #  _________________________________  "How did you feel?" step  ____________________________________
    def set_headache_pain_intensity(self):

        headache_pain_intensity_location = (MobileBy.ID, 'com.migrainemonitor.dev:id/ll_pain_intensity')
        WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(headache_pain_intensity_location))
        TouchAction(self.driver).press(x=108, y=393).move_to(x=713, y=393).release().perform()

    def set_stress_level_before_headache(self):

        stress_level_before_headache_location = (MobileBy.ID, 'com.migrainemonitor.dev:id/linearLayout')
        WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(stress_level_before_headache_location))
        TouchAction(self.driver).press(x=108, y=653).move_to(x=713, y=653).release().perform()

    def select_aura_with_headache(self):
        aura_with_headache_button_location = (
            MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/'
                            'android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/'
                            'android.support.v4.widget.DrawerLayout/android.widget.RelativeLayout/'
                            'android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.ScrollView/'
                            'android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/'
                            'android.widget.ImageView')
        aura_with_headache_button = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(aura_with_headache_button_location))
        aura_with_headache_button.click()

    def select_speech_difficulty_checkbox(self):
        speech_difficulty_checkbox_location = (
            MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/'
                            'android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/'
                            'android.support.v4.widget.DrawerLayout/android.widget.RelativeLayout/'
                            'android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.ScrollView/'
                            'android.view.ViewGroup/android.widget.LinearLayout[3]/'
                            'android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/'
                            'android.widget.CheckBox')
        speech_difficulty_checkbox = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(speech_difficulty_checkbox_location))
        speech_difficulty_checkbox.click()

    def select_visual_checkbox(self):
        visual_checkbox_location = (
            MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/'
                            'android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/'
                            'android.support.v4.widget.DrawerLayout/android.widget.RelativeLayout/'
                            'android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.ScrollView/'
                            'android.view.ViewGroup/android.widget.LinearLayout[3]/'
                            'android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]/'
                            'android.widget.CheckBox')
        visual_checkbox = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(visual_checkbox_location))
        visual_checkbox.click()

    def select_weakness_checkbox(self):
        weakness_checkbox_location = (
            MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/'
                            'android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/'
                            'android.support.v4.widget.DrawerLayout/android.widget.RelativeLayout/'
                            'android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.ScrollView/'
                            'android.view.ViewGroup/android.widget.LinearLayout[3]/'
                            'android.support.v7.widget.RecyclerView/android.widget.LinearLayout[3]/'
                            'android.widget.CheckBox')
        weakness_checkbox = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(weakness_checkbox_location))
        weakness_checkbox.click()


    #   ___________________________  "Pain location" step   _________________________________________
    def select_temporal_right_dot(self):

        temporal_right_dot_location = (MobileBy.ID, 'com.migrainemonitor.dev:id/iv_temporal_right')
        temporal_right_dot = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(temporal_right_dot_location))
        temporal_right_dot.click()

    def select_upper_nape_left_dot(self):
        upper_nape_left_dot_location = (MobileBy.ID, 'com.migrainemonitor.dev:id/iv_upper_nape_left')
        upper_nape_left_dot = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(upper_nape_left_dot_location))
        upper_nape_left_dot.click()

    #   ___________________________  "Possible triggers" step   _________________________________________

    def select_stress_trigger_checkbox(self):
        stress_trigger_checkbox_location = (
            MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/'
                            'android.widget.FrameLayout/android.widget.LinearLayout/'
                            'android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/'
                            'android.widget.RelativeLayout/android.widget.FrameLayout[2]/'
                            'android.view.ViewGroup/android.support.v7.widget.RecyclerView/'
                            'android.widget.LinearLayout[8]/android.widget.CheckBox')
        stress_trigger_checkbox = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(stress_trigger_checkbox_location))
        stress_trigger_checkbox.click()

    def select_little_sleep_trigger_checkbox(self):
        little_sleep_trigger_checkbox_location = (
            MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/'
                            'android.widget.FrameLayout/android.widget.LinearLayout/'
                            'android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/'
                            'android.widget.RelativeLayout/android.widget.FrameLayout[2]/'
                            'android.view.ViewGroup/android.support.v7.widget.RecyclerView/'
                            'android.widget.LinearLayout[9]/android.widget.CheckBox')
        little_sleep_trigger_checkbox = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(little_sleep_trigger_checkbox_location))
        little_sleep_trigger_checkbox.click()

    def click_skip_next_button(self):

        skip_next_button_location = (MobileBy.ID, 'com.migrainemonitor.dev:id/btn_skip_next')
        skip_next_button = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(skip_next_button_location))
        skip_next_button.click()

    #   ___________________________  "Note & Other symptoms" step   __________________________________

    def make_a_note(self, note):

        note_description_location = (MobileBy.ID, 'com.migrainemonitor.dev:id/tv_note_description')
        note_description = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(note_description_location))
        note_description.click()

        edit_message_location = (MobileBy.ID, 'com.migrainemonitor.dev:id/edit_message')
        edit_message = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(edit_message_location))
        edit_message.send_keys(note)

        save_button_location = (MobileBy.ID, 'com.migrainemonitor.dev:id/btn_save')
        save_button = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(save_button_location))
        save_button.click()

    def select_dizziness_checkbox(self):
        dizziness_checkbox_location = (
            MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/'
                            'android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/'
                            'android.support.v4.widget.DrawerLayout/android.widget.RelativeLayout/'
                            'android.widget.FrameLayout[2]/android.view.ViewGroup/'
                            'android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/'
                            'android.widget.CheckBox')
        dizziness_checkbox = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(dizziness_checkbox_location))
        dizziness_checkbox.click()

    def select_light_sensitivity_checkbox(self):
        light_sensitivity_checkbox_location = (
            MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/'
                            'android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/'
                            'android.support.v4.widget.DrawerLayout/android.widget.RelativeLayout/'
                            'android.widget.FrameLayout[2]/android.view.ViewGroup/'
                            'android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]/'
                            'android.widget.CheckBox')
        light_sensitivity_checkbox = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(light_sensitivity_checkbox_location))
        light_sensitivity_checkbox.click()

    def select_nausea_checkbox(self):
        nausea_checkbox_location = (
            MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/'
                            'android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/'
                            'android.support.v4.widget.DrawerLayout/android.widget.RelativeLayout/'
                            'android.widget.FrameLayout[2]/android.view.ViewGroup/'
                            'android.support.v7.widget.RecyclerView/android.widget.LinearLayout[3]/'
                            'android.widget.CheckBox')
        nausea_checkbox = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(nausea_checkbox_location))
        nausea_checkbox.click()

    def select_vomiting_checkbox(self):
        vomiting_checkbox_location = (
            MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/'
                            'android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/'
                            'android.support.v4.widget.DrawerLayout/android.widget.RelativeLayout/'
                            'android.widget.FrameLayout[2]/android.view.ViewGroup/'
                            'android.support.v7.widget.RecyclerView/android.widget.LinearLayout[4]/'
                            'android.widget.CheckBox')
        vomiting_checkbox = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(vomiting_checkbox_location))
        vomiting_checkbox.click()

    #   ___________________________  "Your headache summary" step   __________________________________

    def click_submit_button(self):

        submit_button_location = (MobileBy.ID, 'com.migrainemonitor.dev:id/btn_submit')
        submit_button = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(submit_button_location))
        submit_button.click()

    #   ___________________________  "" step   __________________________________

    def click_done_button(self):
        done_button_location = (MobileBy.ID, 'com.migrainemonitor.dev:id/btn_done')
        done_button = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(done_button_location))
        done_button.click()

