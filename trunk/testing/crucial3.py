"""
爬取ccc网站
"""
# -*- coding:utf-8 -*-
import requests
import logging
import re
import time

from urllib.parse import unquote

__author__ = 'Evan'

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
logger = logging.getLogger(__name__)


class Crawler(object):

    def __init__(self, url=''):
        self.session = requests.Session()
        self.source_url = url
        self.referer_url = 'https://cloudsso.cisco.com/'
        self.duo_security_url = 'https://api-dbbfec7f.duosecurity.com/frame/web/v1/auth?'
        self.verification_source_url = 'https://api-dbbfec7f.duosecurity.com'
        self.verification_prompt_url = self.verification_source_url + '/frame/prompt'
        self.verification_status_url = self.verification_source_url + '/frame/status'
        self.user_agent = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/78.0.3904.97 Safari/537.36'
        }
        self.login_account = ('evaliu', '66Dashun!!')

    def login_ccc(self):
        resp = self.session.get(self.source_url)
        if '302' in str(resp.history):  # 重定向进入账户登陆界面
            login_url = re.search('name="login-form" action="(.+?)"', resp.text)
            data = {
                'pf.username': self.login_account[0],
                'pf.pass': self.login_account[1],
                'pf.userType': 'cco',
                'pf.TargetResource': '?'
            }
            # 进入Login界面 --> https://cloudsso.cisco.com//as/MQW3N/resume/as/authorization.ping
            resp = self.session.post(login_url.group(1), headers=self.user_agent, data=data)
            if resp.status_code == 200:
                self.login_authentication(resp.text)

    def login_authentication(self, resp):
        # 抓取认证参数
        sig_request = re.search("'sig_request': '(.+?):APP", resp)
        post_action = re.search("'post_action': '(.+?)'", resp)
        referer = self.referer_url + post_action.group(1)

        authentic_url = '{}tx={}&parent={}&v={}'.format(self.duo_security_url, sig_request.group(1), referer, '2.6')
        data = {
            'tx': sig_request.group(1),
            'parent': referer,
            'referer': referer,
            'screen_resolution_width': '1920',
            'screen_resolution_height': '1080',
            'color_depth': '24',
            'is_cef_browser': 'false',
            'is_ipad_os': 'false'
        }
        # 进入权限验证界面 --> https://api-dbbfec7f.duosecurity.com/frame/web/v1/auth?
        resp = self.session.post(authentic_url, headers=self.user_agent, data=data)
        if '302' in str(resp.history):  # 重定向进入权限验证界面
            sid = re.search('sid=(.+)', unquote(resp.url))
            # data = {
            #     'sid': sid.group(1),
            #     'device': 'phone1',
            #     'factor: ': 'Passcode',
            #     'passcode: ': '317138',  # 使用手机验证码登陆
            #     'dampen_choice': 'true',
            #     'out_of_date': 'False',
            #     'days_out_of_date': '0',
            #     'days_to_block': 'None'
            # }
            data = {
                'sid': sid.group(1),
                'device': 'phone1',
                'factor': 'Duo Push',
                'dampen_choice': 'true',  # 使用手机push登陆
                'out_of_date': 'False',
                'days_out_of_date': '0',
                'days_to_block': 'None'
            }
            # 开始验证
            resp = self.session.post(self.verification_prompt_url, headers=self.user_agent, data=data)  # prompt
            if resp.status_code == 200:
                # TODO 使用手机登陆验证软件点击approve
                input('Please use the mobile phone login verification software to click approval, and then press enter')
                time.sleep(1)

                data = {
                    'sid': sid.group(1),
                    'txid': resp.json()['response']['txid']
                }
                resp = self.session.post(self.verification_status_url, headers=self.user_agent, data=data)  # Get status
                if resp.status_code == 200:
                    final_url = self.verification_source_url + resp.json()['response']['result_url']
                    data = {
                        'sid': sid.group(1)
                    }
                    resp = self.session.post(final_url, headers=self.user_agent, data=data)  # verify pass
                    if resp.status_code == 200:
                        print('verify pass')
                        print(resp.url)
                        print(resp.history)
                        print(resp.json())
                        parent = resp.json()['response']['parent'] + '?'
                        print('parent: {}'.format(parent))

                        # final
                        headers = {
                            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                                          ' (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
                            'referer': parent
                        }
                        resp = self.session.get('https://cesium.cisco.com/', headers=headers)
                        print('start test record search')
                        print(resp.url)
                        print(resp.status_code)
                        print(resp.history)

                        # getToken
                        # headers = {
                        #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                        #                   '(KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
                        #     'referer': 'https://cesium.cisco.com/apps/cesiumhome/overview'
                        # }
                        # resp = self.session.get('https://cesium.cisco.com/apps/machineservices/MachineDetails.svc/getToken',
                        #                         headers=headers)
                        # print('get token')
                        # print(resp.url)
                        # print(resp.history)
                        # print(resp.json())

                        # get evaliu
                        # resp = self.session.get(
                        #     'https://cesium.cisco.com/svclnx/cgi-bin/polarisappssvc/services.py/getuserappsconfigoptionswithusername/evaliu',
                        #     headers=self.user_agent)
                        # print('get evaliu')
                        # print(resp.url)
                        # print(resp.history)
                        # print(resp.json())

                        # get ccc user details
                        # headers = {
                        #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                        #                   '(KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
                        #     'origin': 'https://cesium.cisco.com',
                        #     'referer': 'https://cesium.cisco.com/apps/cesiumhome/overview',
                        # }
                        # data = {
                        #     'name': 'evaliu'
                        # }
                        # resp = self.session.post(
                        #     'https://cesium.cisco.com/apps/machineservices/MachineDetails.svc/CCCGetUserDetails',
                        #     headers=headers, data=data)
                        # print('ccc get user details')
                        # print(resp.url)
                        # print(resp.history)
                        # print(resp.text)

    def test_record_search(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/78.0.3904.97 Safari/537.36',
            'csession': '17E8F69B-3A3A-4226-9306-3CF7BABCA327',
            'referer': 'https://cesium.cisco.com/apps/cesiumhome/overview'
        }
        resp = self.session.get(self.source_url, headers=headers)
        print('start test record search')
        print(resp.url)
        print(resp.status_code)
        print(resp.history)

    def main(self):
        self.login_ccc()
        # self.test_record_search()


if __name__ == '__main__':
    crawler = Crawler(url='https://cesium.cisco.com/apps/cesiumhome/overview')
    crawler.main()
