from appium.webdriver.common.appiumby import AppiumBy

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import PointerInput
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from behave import given, when
# from behave import given, when, then

class RemoteCollabote:
    def __init__(self, driver):
        self.driver = driver
        
        # 원격 협업 메인 화면
        self.collaborate_main = (
            AppiumBy.XPATH, "//android.widget.TextView[@resource-id='com.virnect.remote.mobile2_onpremise_common:id/home_tv_title' and @text='원격 협업']")
        
        # 원격 협업 리스트 화면
        self.collaborate_list = (AppiumBy.ID, "com.virnect.remote.mobile2_onpremise_common:id/fragment_container")
        
        # 원격 협업 찾기 메뉴
        self.serch_menu = (AppiumBy.ID, "com.virnect.remote.mobile2_onpremise_common:id/home_iv_search")
        
        # 원격 협업 알림 메뉴
        self.alarm_menu = (AppiumBy.ID, "com.virnect.remote.mobile2_onpremise_common:id/home_iv_alarm")
        
        # 원격 협업 알림 메뉴 > 알림 리스트
        self.alarm_list = (AppiumBy.ID, "com.virnect.remote.mobile2_onpremise_common:id/home_cl_root")
        
        # 원격 협업 알림 > 알림 리스트 > 알림 수신
        self.alarm_receive = (AppiumBy.ID, "com.virnect.remote.mobile2_onpremise_common:id/home_tv_toggle_subscribe")
        
        # 원격 협업 알림 > 알림 리스트 > 알림 해제
        self.alarm_release = (AppiumBy.ID, "com.virnect.remote.mobile2_onpremise_common:id/home_tv_toggle_subscribe")
        
        # 알림 리스트 > 이전 버튼
        self.alarm_backbutton = (AppiumBy.ID, "com.virnect.remote.mobile2_onpremise_common:id/home_iv_search")
        
        # 원격 협업 생성 버튼
        self.collaborate_create_btn = (AppiumBy.ID, "com.virnect.remote.mobile2_onpremise_common:id/btn_create_room")
        
        # 오픈룸 생성 버튼
        self.openroom_btn = (AppiumBy.ID, "com.virnect.remote.mobile2_onpremise_common:id/btn_create_open_room")
        
        # Remote Mobile 하단 메뉴
        self.home_menu = (AppiumBy.ID, "com.virnect.remote.mobile2_onpremise_common:id/home_bottom")
        
        # 원격 협업 메뉴
        self.collaborate_menu = (AppiumBy.ID, "com.virnect.remote.mobile2_onpremise_common:id/home_iv_remote_collaboration")
        
        # 최근 기록 메뉴
        self.recent_records = (AppiumBy.ID, "com.virnect.remote.mobile2_onpremise_common:id/home_iv_recent_records")
        
        # 멤버 메뉴
        self.member_menu = (AppiumBy.ID, "com.virnect.remote.mobile2_onpremise_common:id/home_iv_member")
        
        # 환경 설정 메뉴 
        self.preferences_menu = (AppiumBy.ID, "com.virnect.remote.mobile2_onpremise_common:id/home_iv_settings")
        
    @given('Remote Mobile 원격 협업 메인 화면 확인')
    def mobile_collabrate_displayed(self):
        try:
            main_collaborate = WebDriverWait(self.driver, 5).until(
                EC.text_to_be_present_in_element((self.collaborate_main), '원격 협업'))
            if main_collaborate:
                print("원격 협업 메인 화면이 존재합니다.")
            else:
                print("원격 협업 메인 화면이 존재하지 않습니다.")
            return main_collaborate
        except NoSuchElementException:
            print("원격 협업 메인 화면을 찾을 수 없습니다.")
            
    @when('원격 협업 리스트를 새로고침 시도')
    def remote_collaborate_re_flash(self):
        try:
            re_flash = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.collaborate_list)))
            actions = ActionChains(self.driver)
            actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to_location(535, 825)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.move_to_location(532, 1453)
            actions.w3c_actions.pointer_action.release()
            actions.perform()
            print("원격 협업 리스트를 새로고침 했습니다.")
            return re_flash
        except NoSuchElementException:
            print("원격 협업 리스트를 새로고침 했습니다.")
            return False
        
    # @then('원격 협업 생성 메뉴 확인')
    # def remote_collaborate_displayed(self):
    #     try:
    #         remocollabo_create_btn = WebDriverWait(self.driver, 5).until(
    #             EC.presence_of_element_located(()))