from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import PointerInput
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from behave import given, when, then

# Mobile Remote 접근 권한 허용 안내 화면
class Permissions:
    def __init__(self, driver):
        self.driver = driver
        
        # 접근 권한 허용 다이얼 로그창
        self.permission_dialogs = (AppiumBy.ID, "com.virnect.remote.mobile2_onpremise_common:id/mobile_permission_fragment")
        
        # 접근 권한 허용 다이얼 로그창 : [확인]
        self.confirmation = (AppiumBy.ID, "com.virnect.remote.mobile2_onpremise_common:id/permission_btn_confirm")
        
        # 사진 촬영 및 동영상 다이얼 로그창
        self.picture_video = (AppiumBy.ID, "com.android.permissioncontroller:id/grant_dialog")
        
        # 사진 촬영 및 동영상 : [앱 사용 중에만 허용] 터치
        self.pictrecordapp_allow = (AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_foreground_only_button")
        
        # 오디오 녹음 허용 다이얼 로그창
        self.audio_recording = (AppiumBy.ID, "com.android.permissioncontroller:id/grant_dialog")
        
        # 오디오 녹음 : [앱 사용중에만 허용] 터치
        self.AudioRecordapp_allow = (AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_foreground_only_button")
        
        # Remote에서 근처에 있는 기기 연결 및 상대적 위치 파악 다이얼 로그창
        self.devices_location = (AppiumBy.ID, "com.android.permissioncontroller:id/grant_dialog")
        
        # Remote에서 근처에 있는 기기 연결 및 상대적 위치 : [허용] 터치
        self.devicelocatapp_allow = (AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_button")
        
        # VIRNECT Remote에서 기기의 사진, 동영상, 음악, 오디오 액세스 다이얼 로그창
        self.pictvidmusaud = (AppiumBy.ID, "com.android.permissioncontroller:id/grant_dialog")
        
        # VIRNECT Remote에서 기기의 사진, 동영상, 음악, 오디오 액세스 : [허용] 터치
        self.pictvidmusaudapp_allow = (AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_button")
        
        # 화면 공유 시, 다른 앱 위에서 포인팅 > -다른 앱 표시 다이얼 로그창
        self.otherapp_dialog = (AppiumBy.ID, "com.virnect.remote.mobile2_onpremise_common:id/parentPanel")
        
        # 화면 공유 시, 다른 앱 위에서 포인팅 > -다른 앱 표시 다이얼 로그창 : [허용] 터치
        self.otherapp_dialog_set = (AppiumBy.ID, "android:id/button1")
        
        # 다른 앱 위에 표시 리스트에서 Remote 앱 리스트
        self.other_remote = (AppiumBy.XPATH, '//android.widget.LinearLayout[@content-desc="Remote,137MB, 사용 안 함, 스위치"]/android.widget.LinearLayout[2]')
        
        # 다른 앱 위에 표시 리스트에서 Remote 앱 리스트 : [사용함] 터치
        self.switch_used = (AppiumBy.XPATH, '//android.widget.LinearLayout[@content-desc="Remote,140MB, 사용 안 함, 스위치"]/android.widget.LinearLayout[3]/android.widget.LinearLayout/android.widget.Switch')
        
        # 다른 앱 표시 리스트 > [상위 메뉴로 이동 버튼] 터치
        self.up_menu_move = (AppiumBy.XPATH, '//android.widget.ImageButton[@content-desc="상위 메뉴로 이동"]')
        
        # SERVER INFO 다이얼 로그창
        self.server_info = (AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup')
        
        # SERVER INFO 다이얼 로그창 > IP 입력 필드
        self.ip_inputfield = (AppiumBy.ID, "com.virnect.remote.mobile2_onpremise_common:id/server_url_setting_et_ip")
        
        # SERVER INFO 다이얼 로그창 > PORT 입력 필드
        self.port_inputfield = (AppiumBy.ID, "com.virnect.remote.mobile2_onpremise_common:id/server_url_setting_et_port")
        
        # SERVER INFO 다이얼 로그창 > IP 및 PORT 입력 > [확인] 버튼
        self.server_confirmation = (AppiumBy.ID, "com.virnect.remote.mobile2_onpremise_common:id/server_url_setting_btn_confirm")
        
    @given('접근 권한 허용 다이얼 로그창 확인')
    def permission_dialogs_displayed(self):
        try:
            permission = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.permission_dialogs)))
            if permission.is_displayed():
                print("접근 권한 허용 다이얼 로그창 출력되었습니다.")
            else:
                print("접근 권한 허용 다이얼 로그창이 출력되지 않았습니다.")
            return permission.is_displayed
        except NoSuchElementException:
            print("접근 권한 허용 다이얼 로그창을 찾을 수 없습니다.")
            return False
        
    @when('접근 권한 허용 다이얼 로그창에서 [확인] 버튼 확인')
    def confirmation_permission_displayed(self):
        try:
            confirmation_btn = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.confirmation)))
            if confirmation_btn.is_displayed():
                print("접근 권한 허용 다이얼 로그창에 [확인] 버튼이 존재합니다.")
            else:
                print("접근 권한 허용 다이얼 로그창에 [확인] 버튼이 존재하지 않습니다.")
            return confirmation_btn.is_displayed
        except NoSuchElementException:
            print("접근 권한 허용 다이얼 로그창에서 [확인] 버튼을 찾을 수 없습니다.")
        
    @then('접근 권한 허용 종류 다이얼 로그창에서 확인 터치하기')
    def touch_permission_dialog(self):
        try:
            confirmation_touch = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((self.confirmation)))
            actions = ActionChains(self.driver)
            actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to(confirmation_touch)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.pause(0.1)
            actions.w3c_actions.pointer_action.release()
            actions.perform()
            print("접근 권한 허용 다이얼 로그창에서 [확인] 버튼을 터치했습니다.")
            return confirmation_touch
        except NoSuchElementException:
            print("접근 권한 허용 다이얼 로그창에서 [확인] 버튼 터치를 못했습니다.")
            return False
    
    @given('Remote에서 사진 촬영 및 동영상 녹화 허용 다이얼 로그창 확인')
    def picture_recording_modal_displayed(self):
        try:
            picture_recording = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.picture_video)))
            if picture_recording.is_displayed():
                print("사진 촬영 및 동영상 녹화 허용 다이얼 로그창이 존재합니다.")
            else:
                print("사진 촬영 및 동영상 녹화 허용 다이얼 로그창이 존재하지 않습니다.")
            return picture_recording.is_displayed
        except NoSuchElementException:
            print("사진 촬영 및 동영상 녹화 허용 다이얼 로그창을 찾을 수 없습니다.")
            return False
    
    @when('Remote에서 사진 촬영 및 동영상 녹화 다이얼 로그창에서 [앱 사용 중에만 허용 선택하기] 버튼 확인')
    def picture_video_app_allow(self):
        try:
            pictvideo_appallow_btn = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.pictrecordapp_allow)))
            if pictvideo_appallow_btn.is_displayed():
                print("사진 촬영 및 동영상 녹화 다이얼 로그창에서 [앱 사용 중에만 허용 선택하기] 버튼이 존재합니다.")
            else:
                print("사진 촬영 및 동영상 녹화 다이얼 로그창에서 [앱 사용 중에만 허용 선택하기] 버튼이 존재하지 않습니다.")
            return pictvideo_appallow_btn.is_displayed
        except NoSuchElementException:
            print("사진 촬영 및 동영상 녹화 다이얼 로그창에서 [앱 사용 중에만 허용 선택하기] 버튼을 찾을 수 없습니다.")
            return False
            
    @then('Remote에서 사진 촬영 및 동영상 녹화 다이얼 로그창에서 [앱 사용 중에만 허용 선택하기] 터치하기')
    def touch_picture_recording_displayed(self):
        try:
            recording_appallow_touch = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((self.pictrecordapp_allow)))
            actions = ActionChains(self.driver)
            actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to(recording_appallow_touch)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.pause(0.1)
            actions.w3c_actions.pointer_action.release()
            actions.perform()
            print("사진 촬영 및 동영상 녹화 다이얼 로그창에서 [앱 사용 중에만 허용] 버튼을 터치했습니다.")
            return recording_appallow_touch
        except NoSuchElementException:
            print("녹화 허용 다이얼 로그창에서 [앱 사용 중에만 허용] 버튼 터치를 못했습니다.")
            return False
        
    @given('Remote에서 오디오를 녹음 허용 다이얼 로그창 확인')
    def audio_recording_modal_displayed(self):
        try:
            audio_recording  = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.audio_recording)))
            if audio_recording.is_displayed():
                print("오디오 녹음 허용 다이얼 로그창이 존재합니다.")
            else:
                print("오디오 녹음 허용 다이얼 로그창이 존재하지 않습니다.")
            return audio_recording.is_displayed
        except NoSuchElementException:
            print("오디오 녹음 허용 다이얼 로그창을 찾을 수 없습니다.")
            return False
    
    @when('Remote에서 오디오를 녹음 허용 다이얼 로그창에서 [앱 사용중에만 허용] 버튼 확인')
    def audio_recording_appallow_displayed(self):
        try:
            audiorecording_btn = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.AudioRecordapp_allow)))
            if audiorecording_btn.is_displayed():
                print("오디오 녹음 허용 다이얼 로그창에서 [앱 사용중에만 허용] 버튼이 존재합니다.")
            else:
                print("오디오 녹음 허용 다일얼 로그창에서 [앱 사용중에만 허용] 버튼이 존재하지 않습니다.")
            return audiorecording_btn.is_displayed
        except NoSuchElementException:
            print("오디오 녹음 허용 다일얼 로그창에서 [앱 사용중에만 허용] 버튼을 찾을 수 없습니다.")
            
    @then('Remote에서 오디오를 녹음 허용 다이얼 로그창에서 [앱 사용중에만 허용] 버튼 터치하기')
    def touch_audio_recording(self):
        try:
            audiorecording_touch = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((self.AudioRecordapp_allow )))
            actions = ActionChains(self.driver)
            actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to(audiorecording_touch)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.pause(0.1)
            actions.w3c_actions.pointer_action.release()
            actions.perform()
            print("녹화 허용 다이얼 로그창에서 [앱 사용 중에만 허용] 버튼을 터치했습니다.")
            return audiorecording_touch
        except NoSuchElementException:
            print("녹화 허용 다이얼 로그창에서 [앱 사용 중에만 허용] 버튼 터치를 못했습니다.")
            return False
        
    @given('Remote에서 근처에 있는 기기 연결 및 상대적 위치 파악 다이얼 로그창 확인')
    def devices_location_displayed(self):
            try:
                devices_location = WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((self.devices_location)))
                if devices_location.is_displayed():
                    print("기기 연결 및 상대적 위치 파악 다이얼 로그창이 존재합니다.")
                else:
                    print("기기 연결 및 상대적 위치 파악 다이얼 로그창이 존재하지 않습니다.")
                return devices_location.is_displayed
            except NoSuchElementException:
                print("기기 연결 및 상대적 위치 파악 다이얼 로그창을 찾을 수 없습니다.")
                return False
            
    @when('Remote에서 근처에 있는 기기 연결 및 상대적 위치 파악 다이얼 로그창에서 [허용] 버튼 확인')
    def devices_location_allow_displayed(self):
        try:
            deviceslocation_allow = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.devicelocatapp_allow)))
            if deviceslocation_allow.is_displayed():
                print("기기 연결 및 상대적 위치 파악 다이얼 로그창에 [허용] 버튼이 존재합니다.")
            else:
                print("기기 연결 및 상대적 위치 파악 다이얼 로그창에 [허용] 버튼이 존재하지 않습니다.")
            return deviceslocation_allow.is_displayed
        except NoSuchElementException:
            print("기기 연결 및 상대적 위치 파악 다이얼 로그창에서 [허용] 버튼을 찾을 수 없습니다.")
            return False
        
    @then('Remote에서 근처에 있는 기기 연결 및 상대적 위치 파악 다이얼 로그창에서 [허용] 버튼 터치하기')
    def touch_devices_location_allow(self):
        try:
            deviceslocation_touch = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((self.devicelocatapp_allow)))
            actions = ActionChains(self.driver)
            actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to(deviceslocation_touch)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.pause(0.1)
            actions.w3c_actions.pointer_action.release()
            actions.perform()
            print("상대적 위치 파악 허용 다이얼 로그창에서 [허용] 버튼을 터치했습니다.")
            return deviceslocation_touch
        except NoSuchElementException:
            print("상대적 위치 파악 허용 다이얼 로그창에서 [허용] 버튼 터치를 못했습니다.")
            return False
        
    @given('Remote에서 기기의 사진, 동영상, 음악, 오디오 액세스 다이얼 로그창 확인')
    def pictu_video_mus_audio_displayed(self):
        try:
            pict_vid_mus_aud = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.pictvidmusaud)))
            if pict_vid_mus_aud.is_displayed():
                print("기기의 사진, 동영상, 음악, 오디오 액세스 허용 다이얼 로그창이 존재합니다.")
            else:
                print("기기의 사진, 동영상, 음악, 오디오 액세스 허용 다이얼 로그창이 존재하지 않습니다.")
            return pict_vid_mus_aud.is_displayed
        except NoSuchElementException:
            print("기기의 사진, 동영상, 음악, 오디오 액세스 허용 다이얼 로그창을 찾을 수 없습니다.")
            return False
    
    @when('Remote에서 기기의 사진, 동영상, 음악, 오디오 액세스 다이얼 로그창에서 [허용] 버튼 확인')
    def picvidmusaud_allow_displayed(self):
        try:
            picvidmusaud_allow = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.pictvidmusaudapp_allow)))
            if picvidmusaud_allow.is_displayed():
                print("기기의 사진, 동영상, 음악, 오디오 액세스 다이얼 로그창에 [허용] 버튼이 존재합니다.")
            else:
                print("기기의 사진, 동영상, 음악, 오디오 액세스 다이얼 로그창에 [허용] 버튼이 존재하지 않습니다.")
            return picvidmusaud_allow.is_displayed
        except NoSuchElementException:
            print("기기의 사진, 동영상, 음악, 오디오 액세스 다이얼 로그창에서 [허용] 버튼을 찾을 수 없습니다.")
            return False
        
    @then('Remote에서 기기의 사진, 동영상, 음악, 오디오 액세스 다이얼 로그창에서 [허용] 버튼 터치하기')
    def touch_picvidmusaud_allow(self):
        try:
            picvidmusaud_touch = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((self.pictvidmusaudapp_allow)))
            actions = ActionChains(self.driver)
            actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to(picvidmusaud_touch)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.pause(0.1)
            actions.w3c_actions.pointer_action.release()
            actions.perform()
            print("기기의 사진 및 미디어 액세스 허용 다이얼 로그창에서 [허용] 버튼을 터치했습니다.")
            return picvidmusaud_touch
        except NoSuchElementException:
            print("기기의 사진 및 미디어 액세스 허용 다이얼 로그창에서 [허용] 버튼 터치를 못했습니다.")
            return False
        
    @given('화면 공유 시, 다른 앱 위에서 포인팅 > -다른 앱 표시 다이얼 로그창 확인')
    def other_app_pointing_displayed(self):
        try:
            otherapp_pointing = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.otherapp_dialog)))
            if otherapp_pointing.is_displayed():
                print("다른 앱 표시 다이얼 로그창이 존재합니다.")
            else:
                print("다른 앱 표시 다이얼 로그창이 존재하지 않습니다.")
            return otherapp_pointing.is_displayed
        except NoSuchElementException:
            print("다른 앱 표시 다이얼 로그창을 찾을 수 없습니다.")
            return False
        
    # @when('화면 공유 시, 다른 앱 위에서 포인팅 > -다른 앱 표시 다이얼 로그창에서 [허용] 버튼 확인')
    # # self.otherapp_dialog
    # @then('화면 공유 시, 다은 앱 위에서 포인팅 > -다른 앱 표시 다이얼 로그창에서 [허용] 버튼 터치하기')
    # # self.otherapp_dialog_set
    # @given('다른 앱 위에 표시 리스트에서 Remote 리스트 확인')
    # # self.other_remote
    # @when('다른 앱 표시 리스트에서 Remote 앱 리스트 : [사용함] 버튼 확인')
    # # self.switch_used
    # @then('다른 앱 표시 리스트에서 Remote 앱 리스트 : [사용함] 버튼 터치하기')
    # # self.switch_used
    # @given('다른 앱 표시 리스트 > [상위 메뉴로 이동] 버튼 확인')
    # # self.up_menu_mov
    # @when('다른 앱 표시 리스트 > [상위 메뉴로 이동] 버튼 터치하기')
    # # self.up_menu_mov
    
    @given('SERVER INFO 다이얼 로그창 확인')
    def server_info_displayed(self):
        try:
            server_info = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.server_info)))
            if server_info.is_displayed():
                print("SERVER INFO 다이얼 로그창이 존재합니다.")
            else:
                print("SERVER INFO 다이얼 로그창이 존재하지 않습니다.")
            return server_info.is_displayed
        except NoSuchElementException:
            print("SERVER INFO 다이얼 로그창을 찾을 수 없습니다.")
            return False
        
    @when('SERVER INFO 다이얼 로그창에서 IP 입력 필드 확인')
    def server_info_ipinput_displayed(self):
        try:
            ip = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.ip_inputfield)))
            if ip.is_displayed():
                print("SERVER INFO 다이얼 로그창에 IP 입력 필드가 존재합니다.")
            else:
                print("SERVER INFO 다이얼 로그창에 IP 입력 필드가 존재하지 않습니다.")
            return ip.is_displayed
        except NoSuchElementException:
            print("SERVER INFO 다이얼 로그창에 IP 입력 필드를 찾을 수 없습니다.")
            return False
        
    @when('SERVER INFO 다이얼 로그창에서 PORT 입력 필드 확인')
    def server_info_portinput_displayed(self):
        try:
            port = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.ip_inputfield)))
            if port.is_displayed():
                print("SERVER INFO 다이얼 로그창에 PORT 입력 필드가 존재합니다.")
            else:
                print("SERVER INFO 다이얼 로그창에 PORT 입력 필드가 존재하지 않습니다.")
            return port.is_displayed
        except NoSuchElementException:
            print("SERVER INFO 다이얼 로그창에서 PORT 입력 필드을 찾을 수 없습니다.")
            return False
        
    @when('SERVER INFO 다이얼 로그창에서 [확인] 버튼 확인')
    def confirmationbtn_server_info_displayed(self):
        try:
            confirmation_displayed = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.server_confirmation)))
            if confirmation_displayed.is_displayed():
                print("SERVER INFO 다이얼 로그창에 [확인] 버튼이 존재합니다.")
            else:
                print("SERVER INFO 다이얼 로그창에 [확인] 버튼이 존재하지 않습니다.")
            return confirmation_displayed.is_displayed
        except NoSuchElementException:
            print("SERVER INFO 다이얼 로그창에서 [확인] 버튼을 찾을 수 없습니다.")
            return False
        
    @then('SERVER INFO 다이얼 로그창에서 IP 입력 필드에서 텍스트 지우기')
    def ip_clear_server_info(self):
        try:
            ip_clear = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.ip_inputfield)))
            ip_clear.clear()
            print("SERVER INFO 다이얼 로그창 IP 입력 필드에서 텍스트를 지웠습니다.")
            return ip_clear
        except NoSuchElementException:
            print("SERVER INFO 다이얼 로그창 IP 입력 필드에서 텍스트를 지우지 못했습니다.")
            return False
        
    @then('SERVER INFO 다이얼 로그창에서 IP 입력하기')
    def ip_input_server_info(self, serverip):
        try:
            ip_input = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((self.ip_inputfield)))
            ip_input.send_keys(serverip)
            print(f"서버 IP {serverip}가 입력이 되었습니다.")
            return ip_input
        except NoSuchElementException:
            print(f"서버 IP {serverip}가 입력되지 않았습니다.")
            return False
        
    @then('SERVER INFO 다이얼 로그창에서 PORT 입력 필드에서 텍스트 지우기')
    def port_clear_server_info(self):
        try:
            port_clear = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.port_inputfield)))
            port_clear.clear()
            print("SERVER INFO 다이얼 로그창 PORT 입력 필드에서 텍스트를 지웠습니다.")
            return port_clear
        except NoSuchElementException:
            print("SERVER INFO 다이얼 로그창 PORT 입력 필드에서 텍스트를 지우지 못했습니다.")
            return False
        
    @then('SERVER INFO 다이얼 로그창에서 PORT 입력하기')
    def port_input_server_info(self, serverport):
        try:
            port_input = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((self.port_inputfield)))
            port_input.send_keys(serverport)
            print(f"서버 PORT {serverport}가 입력이 되었습니다.")
            return port_input
        except NoSuchElementException:
            print(f"서버 PORT {serverport}가 입력되지 못했습니다.")
            return False
        
    @then('SERVER INFO 다이얼 로그창에서 [확인] 버튼 터치하기')
    def touch_confirmation_server_info(self):
        try:
            confirmation_touch = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((self.server_confirmation)))
            actions = ActionChains(self.driver)
            actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to(confirmation_touch)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.pause(0.1)
            actions.w3c_actions.pointer_action.release()
            actions.perform()
            print("SERVER INFO 다이얼 로그창에서 확인 버튼을 터치했습니다.")
            return confirmation_touch
        except NoSuchElementException:
            print("SERVER INFO 다이얼 로그창에서 확인 버튼 터치를 못했습니다.")
            return False