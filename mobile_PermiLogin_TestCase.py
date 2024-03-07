import unittest
import HtmlTestRunner

from appium import webdriver
from appium.options.common import AppiumOptions
# from appium.options.android import UiAutomator2Options

# from mobile_class.RemoteMoiblePermi import Permissions
# from mobile_class.RemoteMobileLogin import RemoteLogin
from mobile_class.RemoteMobileDisplay import RemoteCollabote

# Mobile Remote 접근 권한 허용 및 로그인
class PermissionsLoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 초기화 작업을 수행하는 부분
        cls.driver = webdriver.Remote('http://127.0.0.1:4723', options=cls.get_capabilities())
        
    @classmethod
    def tearDownClass(cls):
        # 정리 작업을 수행하는 부분
        # if cls.driver:
        #     cls.driver.quit()
        pass
            
    @classmethod
    def get_capabilities(cls):
        return AppiumOptions().load_capabilities(
            {
                "deviceName": "Galaxy S22",
                "platformName": "Android",
                "platformVersion": "14",
                "automationName": "UiAutomator2",
                "app": "C:/PV_REMOTE_v2.9/remote_mobile_2900009.apk",
                "newCommandTimeout": "3000",
                "noReset": "true",
                "appWaitActivity": "*"
            }
        )
        
    def setUp(self):
        # 각 테스트 메소드 실행 전에 초기화 작업을 수행하는 부분
        # 3초간 암묵적 대기 설정
        self.driver.implicitly_wait(3)
        # pass
    
    def tearDown(self):
        # 각 테스트 메소드 실행 후에 정리 작업을 수행하는 부분
        pass
    
    # Remote 접근 권한 허용
    # def test_Permissions(self):
    #     dail_permission = Permissions(self.driver)
        
    #     # 접근 권한 허용 다이얼 로그창 확인
    #     dail_permission.permission_dialogs_displayed()
        
    #     # 3초간 암묵적 대기
    #     self.driver.implicitly_wait(time_to_wait=3)
        
    #     # 접근 권한 허용 다이얼 로그창에서 [확인] 버튼 확인
    #     dail_permission.confirmation_permission_displayed()
        
    #     # 3초간 암묵적 대기
    #     self.driver.implicitly_wait(time_to_wait=3)
        
    #     # 접근 권한 허용 종류 다이얼 로그창에서 확인 터치하기
    #     dail_permission.touch_permission_dialog()
        
    #     # 3초간 암묵적 대기
    #     self.driver.implicitly_wait(time_to_wait=3)
        
    #     # Remote에서 사진 촬영 및 동영상 녹화 허용 다이얼 로그창 확인
    #     dail_permission.picture_recording_modal_displayed()
        
    #     # 3초간 암묵적 대기
    #     self.driver.implicitly_wait(time_to_wait=3)
        
    #     # Remote에서 사진 촬영 및 동영상 녹화 다이얼 로그창에서 [앱 사용 중에만 허용 선택하기] 버튼 확인
    #     dail_permission.picture_video_app_allow()
        
    #     # 3초간 암묵적 대기
    #     self.driver.implicitly_wait(time_to_wait=3)
        
    #     # Remote에서 사진 촬영 및 동영상 녹화 다이얼 로그창에서 [앱 사용 중에만 허용 선택하기] 터치하기
    #     dail_permission.touch_picture_recording_displayed()
        
    #     # 3초간 암묵적 대기
    #     self.driver.implicitly_wait(time_to_wait=3)
        
    #     # Remote에서 오디오를 녹음 허용 다이얼 로그창 확인
    #     dail_permission.audio_recording_modal_displayed()
        
    #     # 3초간 암묵적 대기
    #     self.driver.implicitly_wait(time_to_wait=3)
        
    #     # Remote에서 오디오를 녹음 허용 다이얼 로그창에서 [앱 사용중에만 허용] 버튼 확인
    #     dail_permission.audio_recording_appallow_displayed()
        
    #     # 3초간 암묵적 대기
    #     self.driver.implicitly_wait(time_to_wait=3)
        
    #     # Remote에서 오디오를 녹음 허용 다이얼 로그창에서 [앱 사용중에만 허용] 버튼 터치하기
    #     dail_permission.touch_audio_recording()
        
    #     # 3초간 암묵적 대기
    #     self.driver.implicitly_wait(time_to_wait=3)
        
    #     # Remote에서 근처에 있는 기기 연결 및 상대적 위치 파악 다이얼 로그창 확인
    #     dail_permission.devices_location_displayed()
        
    #     # 3초간 암묵적 대기
    #     self.driver.implicitly_wait(time_to_wait=3)
        
    #     # Remote에서 근처에 있는 기기 연결 및 상대적 위치 파악 다이얼 로그창에서 [허용] 버튼 확인
    #     dail_permission.devices_location_allow_displayed()
        
    #     # 3초간 암묵적 대기
    #     self.driver.implicitly_wait(time_to_wait=3)
        
    #     # Remote에서 근처에 있는 기기 연결 및 상대적 위치 파악 다이얼 로그창에서 [허용] 버튼 터치하기
    #     dail_permission.touch_devices_location_allow()
        
    #     # 3초간 암묵적 대기
    #     self.driver.implicitly_wait(time_to_wait=3)
        
    #     # Remote에서 기기의 사진, 동영상, 음악, 오디오 액세스 다이얼 로그창 확인
    #     dail_permission.pictu_video_mus_audio_displayed()
        
    #     # 3초간 암묵적 대기
    #     self.driver.implicitly_wait(time_to_wait=3)
        
    #     # Remote에서 기기의 사진, 동영상, 음악, 오디오 액세스 다이얼 로그창에서 [허용] 버튼 확인
    #     dail_permission.picvidmusaud_allow_displayed()
        
    #     # 3초간 암묵적 대기
    #     self.driver.implicitly_wait(time_to_wait=3)
        
    #     # Remote에서 기기의 사진, 동영상, 음악, 오디오 액세스 다이얼 로그창에서 [허용] 버튼 터치하기
    #     dail_permission.touch_picvidmusaud_allow()
        
    #     # 3초간 암묵적 대기
    #     self.driver.implicitly_wait(time_to_wait=3)
        
    #     # SERVER INFO 다이얼 로그창 확인
    #     dail_permission.server_info_displayed()
        
    #     # 3초간 암묵적 대기
    #     self.driver.implicitly_wait(time_to_wait=3)
        
    #     # SERVER INFO 다이얼 로그창에서 IP 입력 필드 확인
    #     dail_permission.server_info_ipinput_displayed()
        
    #     # 3초간 암묵적 대기
    #     self.driver.implicitly_wait(time_to_wait=3)
        
    #     # SERVER INFO 다이얼 로그창에서 PORT 입력 필드 확인
    #     dail_permission.server_info_portinput_displayed()
        
    #     # 3초간 암묵적 대기
    #     self.driver.implicitly_wait(time_to_wait=3)
        
    #     # SERVER INFO 다이얼 로그창에서 [확인] 버튼 확인
    #     dail_permission.confirmationbtn_server_info_displayed()
        
    #     # SERVER INFO > ip 및 port 정보
    #     ip_number = '192.168.0.212'
    #     port_number = '8073'
        
    #     # 3초간 암묵적 대기
    #     self.driver.implicitly_wait(time_to_wait=3)
        
    #     # SERVER INFO 다이얼 로그창에서 IP 입력 필드에서 텍스트 지우기
    #     dail_permission.ip_clear_server_info()
        
    #     # 3초간 암묵적 대기
    #     self.driver.implicitly_wait(time_to_wait=3)
        
    #     # SERVER INFO 다이얼 로그창에서 IP 입력하기
    #     dail_permission.ip_input_server_info(ip_number)
        
    #     # 3초간 암묵적 대기
    #     self.driver.implicitly_wait(time_to_wait=3)
        
    #     # SERVER INFO 다이얼 로그창에서 PORT 입력 필드에서 텍스트 지우기
    #     dail_permission.port_clear_server_info()
        
    #     # 3초간 암묵적 대기
    #     self.driver.implicitly_wait(time_to_wait=3)
        
    #     # SERVER INFO 다이얼 로그창에서 PORT 입력하기
    #     dail_permission.port_input_server_info(port_number)
        
    #     # 3초간 암묵적 대기
    #     self.driver.implicitly_wait(time_to_wait=3)
        
    #     # SERVER INFO 다이얼 로그창에서 [확인] 버튼 터치하기
    #     dail_permission.touch_confirmation_server_info()
        
    # # Remote 로그인 화면에서 로그인
    # def test_RemoteLogin(self):
    #     remote_login = RemoteLogin(self.driver)
        
    #     # Remote 로그인 화면 확인
    #     remote_login.login_screen_displayed()
        
    #     # 3초동안 암묵적 대기
    #     self.driver.implicitly_wait(time_to_wait=3)
        
    #     # Remote 로그인 화면에서 아이디 입력 필드 확인
    #     remote_login.id_inputfield_displayed()
        
    #     # 3초동안 암묵적 대기
    #     self.driver.implicitly_wait(time_to_wait=3)
        
    #     # Mobile 아이디 및 패스워드 정보
    #     user_id = 'user2'
    #     user_pw = 'Admin1324'
        
    #     # Remote 로그인 화면에서 아이디 입력하기
    #     remote_login.login_id_input(user_id)
        
    #     # 3초동안 암묵적 대기
    #     self.driver.implicitly_wait(time_to_wait=3)
        
    #     # Remote 로그인 화면에서 패스워드 입력 필드 확인
    #     remote_login.pw_inputfield_displayed()
        
    #     # 3초동안 암묵적 대기
    #     self.driver.implicitly_wait(time_to_wait=3)
        
    #     # Remote 로그인 화면에서 패스워드 입력하기
    #     remote_login.login_pw_input(user_pw)
        
    #     # 3초동안 암묵적 대기
    #     self.driver.implicitly_wait(time_to_wait=3)
        
    #     # Remote  로그인 화면에서 로그인 버튼 확인
    #     remote_login.loging_button_displayed()
        
    #     # 3초동안 암묵적 대기
    #     self.driver.implicitly_wait(time_to_wait=3)
        
    #     # Remote 로그인 화면에서 로그인 버튼 터치하기
    #     remote_login.touch_loging_button()
        
    #     # 워크스페이스 선택 모달창 확인
    #     remote_login.workspace_modal_displayed()
        
    #     # 3초동안 암묵적 대기
    #     self.driver.implicitly_wait(time_to_wait=3)
        
    #     # 워크스페이스 선택 모달창에서 My Workspace 선택하기
    #     remote_login.touch_my_workspace()
        
    # Remote Mobile 원격 협업 메인 화면
    def test_RemoteCollabote(self):
        remote_main = RemoteCollabote(self.driver)
        
    # Remote Mobile 원격 협업 메인 화면 확인
        remote_main.mobile_collabrate_displayed()
    
    # 원격 협업 리스트를 새로고침 시도'
        remote_main.remote_collaborate_re_flash()
    
    # 
    
    # 
if __name__ == '__main__':
    reportFolder = "ReportTest"
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=reportFolder))