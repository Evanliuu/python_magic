"""
爬取ccc网站
"""
import time
import logging

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

__author__ = 'Evan'

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
logger = logging.getLogger(__name__)


class CCCSpider(object):

    def __init__(self, url=''):
        self.driver = webdriver.Chrome()  # 初始化driver
        self.waiting = WebDriverWait(self.driver, 60)  # 设置显示等待60秒
        self.driver.implicitly_wait(60)  # 设置隐示等待60秒
        self.source_url = url
        self.account = ('evaliu', '66Dashun!!')  # Login account

    def switch_to_windows(self, to_parent_windows=False):
        """
        切换到不同的windows窗口
        :param to_parent_windows: 默认为False，如果设置为True则回到主窗口
        :return:
        """
        total = self.driver.window_handles
        if to_parent_windows:
            self.driver.switch_to.window(total[0])
        else:
            current_windows = self.driver.current_window_handle
            for window in total:
                if window != current_windows:
                    self.driver.switch_to.window(window)

    def switch_to_frame(self, index=0, to_parent_frame=False, to_default_frame=False):
        """
        切换到不同的frame框架
        :param index: expect by frame index value or id or name or webelement
        :param to_parent_frame: 默认为False，如果设置为True则切换到上一个frame框架
        :param to_default_frame: 默认为False，如果设置为True则切换到最上层的frame框架
        :return:
        """
        if to_parent_frame:
            self.driver.switch_to.parent_frame()
        elif to_default_frame:
            self.driver.switch_to.default_content()
        else:
            self.driver.switch_to.frame(index)

    def close_current_windows(self):
        # 关闭当前页面
        if self.driver:
            self.driver.close()

    def quit_browser(self):
        # 退出所有页面
        if self.driver:
            self.driver.quit()

    def login_ccc(self):
        """
        Login ccc website
        :return:
        """
        self.driver.get(self.source_url)
        # Login CCC
        username = self.waiting.until(EC.presence_of_element_located((By.XPATH, '//*[@id="userInput"]')))
        username.send_keys(self.account[0])
        self.waiting.until(EC.presence_of_element_located((By.XPATH, '//*[@id="login-button"]'))).click()
        password = self.waiting.until(EC.presence_of_element_located((By.XPATH, '//*[@id="passwordInput"]')))
        password.send_keys(self.account[1])
        self.waiting.until(EC.presence_of_element_located((By.XPATH, '//*[@id="login-button"]'))).click()
        # safety certificate
        self.switch_to_frame()
        self.waiting.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="login-form"]/div[2]/div/label/input'))).click()
        self.waiting.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="auth_methods"]/fieldset/div[1]/button'))).click()

    def test_record_search(self, sn):
        """
        Test record search
        :param sn:
        :return:
        """
        # input information
        search_text = self.waiting.until(EC.presence_of_element_located((By.XPATH, '//*[@id="searchText"]')))
        search_text.send_keys(sn)
        search_text.send_keys(Keys.ENTER)
        # click measures
        time.sleep(5)
        self.waiting.until(EC.presence_of_element_located((By.XPATH, '//*[@id="example-one"]/span[3]/a'))).click()
        time.sleep(5)

    def parse(self):
        html = self.driver.page_source
        soup = BeautifulSoup(html, 'lxml')
        nodes = soup.find_all('a', class_='ui-grid-canvas')
        logger.info('nodes: {}'.format(nodes))

    def main(self):
        self.login_ccc()
        # self.test_record_search(sn='FOC23324CB2')
        # self.parse()


if __name__ == '__main__':
    spider = CCCSpider(url='https://cesium.cisco.com/')
    spider.main()
