import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

"""webdriver模块12个常用方法-------------------------
1.  set_window_size()	    设置浏览器的大小
2.  back()	                控制浏览器后退
3.  forward()	            控制浏览器前进
4.  refresh()	            刷新当前页面
5.  clear()	                清除文本
6.  send_keys (value)	    模拟按键输入
7.  click()	                单击元素
8.  submit()	            用于提交表单
9.  get_attribute(name)	    获取元素属性值
10. is_displayed()	        设置该元素是否用户可见
11. size	                返回元素的尺寸
12. text	                获取元素的文本
--------------------------------------------------
"""

"""定位元素的8种方式-------------------------------------------------------------------------------
定位一个元素:                             定位多个元素:                           含义：
1. find_element_by_id	                find_elements_by_id	                  通过元素id定位
2. find_element_by_name	                find_elements_by_name	              通过元素name定位
3. find_element_by_xpath	            find_elements_by_xpath	              通过xpath表达式定位
4. find_element_by_link_text	        find_elements_by_link_tex	          通过完整超链接定位
5. find_element_by_partial_link_text	find_elements_by_partial_link_text	  通过部分链接定位
6. find_element_by_tag_name	            find_elements_by_tag_name	          通过标签定位
7. find_element_by_class_name	        find_elements_by_class_name	          通过类名进行定位
8. find_elements_by_css_selector	    find_elements_by_css_selector	      通过css选择器进行定位
---------------------------------------------------------------------------------------------------
"""

"""expected_conditions 17个判断条件函数--------------------------------------------------------
以下两个条件类验证title，验证传入的参数title是否等于或包含于driver.title 
1. title_is 
2. title_contains

以下两个条件验证元素是否出现，传入的参数都是元组类型的locator，如(By.ID, ‘kw’) 
顾名思义，一个只要一个符合条件的元素加载出来就通过；另一个必须所有符合条件的元素都加载出来才行 
3. presence_of_element_located 
4. presence_of_all_elements_located

以下三个条件验证元素是否可见，前两个传入参数是元组类型的locator，第三个传入WebElement 
第一个和第三个其实质是一样的 
5. visibility_of_element_located 
6. invisibility_of_element_located 
7. visibility_of

以下两个条件判断某段文本是否出现在某元素中，一个判断元素的text，一个判断元素的value 
8. text_to_be_present_in_element 
9. text_to_be_present_in_element_value

以下条件判断frame是否可切入，可传入locator元组或者直接传入定位方式：id、name、index或WebElement 
10. frame_to_be_available_and_switch_to_it

以下条件判断是否有alert出现 
11. alert_is_present

以下条件判断元素是否可点击，传入locator 
12. element_to_be_clickable

以下四个条件判断元素是否被选中，第一个条件传入WebElement对象，第二个传入locator元组 
第三个传入WebElement对象以及状态，相等返回True，否则返回False 
第四个传入locator以及状态，相等返回True，否则返回False 
13. 13. element_to_be_selected 
14. element_located_to_be_selected 
15. element_selection_state_to_be 
16. element_located_selection_state_to_be

最后一个条件判断一个元素是否仍在DOM中，传入WebElement对象，可以判断页面是否刷新了 
17. staleness_of
-----------------------------------------------------------------------------------------------
"""


class Browser(object):

    def __init__(self, url=''):
        self.url = url
        self.drive = webdriver.Chrome()
        self.waiting = None

    def switch_to_windows(self, to_parent_windows=False):
        """
        切换到不同的windows窗口
        :param to_parent_windows: 回到主窗口 if True
        :return:
        """
        total = self.drive.window_handles
        if to_parent_windows:
            self.drive.switch_to.window(total[0])
        else:
            current_windows = self.drive.current_window_handle
            for window in total:
                if window != current_windows:
                    self.drive.switch_to.window(window)

    def switch_to_frame(self, index=0, to_parent_frame=False, to_default_frame=False):
        """
        切换到不同的frame框架
        :param index: expect by frame index value or id or name or webelement
        :param to_parent_frame: 切换到上一个frame框架 if True
        :param to_default_frame: 切换到最上层的frame框架 if True
        :return:
        """
        if to_parent_frame:
            self.drive.switch_to.parent_frame()
        elif to_default_frame:
            self.drive.switch_to.default_content()
        else:
            self.drive.switch_to.frame(index)

    def open_new_windows(self, url=''):
        """
        打开一个新的windows窗口
        :param url: expect new url
        :return:
        """
        js = "window.open({})".format(url)
        self.drive.execute_script(js)
        time.sleep(2)

    def close_current_windows(self):
        if self.drive:
            self.drive.close()

    def quit_browser(self):
        if self.drive:
            self.drive.quit()

    def open_url(self):
        """
        Set the page timeout and execute the default URL
        :return:
        """
        # 显示等待10秒
        self.waiting = WebDriverWait(self.drive, 10)
        # 隐示等待10秒
        self.drive.implicitly_wait(10)
        # 打开url
        self.drive.get(self.url)

    def main(self):
        self.open_url()
        # TODO 普通定位
        # enter = self.drive.find_element_by_xpath('//*[@id="kw"]')
        # 通过验证元素是否出现定位
        enter = self.waiting.until(EC.presence_of_element_located((By.XPATH, '//*[@id="kw"]')))
        # 模拟输入文本
        enter.send_keys('python')
        # 执行输入
        enter.send_keys(Keys.ENTER)
        # 得到网页html
        html = self.drive.page_source
        print('find html:\n', html)
        time.sleep(5)
        # 退出浏览器
        self.quit_browser()


if __name__ == '__main__':
    browser = Browser(url='http://baidu.com')
    browser.main()
