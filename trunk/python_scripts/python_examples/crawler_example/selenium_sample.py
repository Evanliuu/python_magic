"""WebDriver模块12个常用方法:
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

定位元素的8种方式:
定位一个元素:                             定位多个元素:                           含义：
1. find_element_by_id	                find_elements_by_id	                  通过元素id定位
2. find_element_by_name	                find_elements_by_name	              通过元素name定位
3. find_element_by_xpath	            find_elements_by_xpath	              通过xpath表达式定位
4. find_element_by_link_text	        find_elements_by_link_tex	          通过完整超链接定位
5. find_element_by_partial_link_text	find_elements_by_partial_link_text	  通过部分链接定位
6. find_element_by_tag_name	            find_elements_by_tag_name	          通过标签定位
7. find_element_by_class_name	        find_elements_by_class_name	          通过类名进行定位
8. find_elements_by_css_selector	    find_elements_by_css_selector	      通过css选择器进行定位

expected_conditions 17个判断条件函数:
以下两个条件类验证title，验证传入的参数title是否等于或包含于driver.title
1. title_is
2. title_contains

以下两个条件验证元素是否出现，传入的参数都是元组类型的locator，如(By.ID, ‘kw’)
顾名思义，一个只要一个符合条件的元素加载出来就通过；另一个必须所有符合条件的元素都加载出来才行
3. presence_of_element_located
4. presence_of_all_elements_located

以下三个条件验证元素是否可见
前两个传入参数是元组类型的locator
第三个传入WebElement
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

以下四个条件判断元素是否被选中，
第一个条件传入WebElement对象，
第二个传入locator元组,
第三个传入WebElement对象以及状态，相等返回True，否则返回False,
第四个传入locator以及状态，相等返回True，否则返回False
13. element_to_be_selected
14. element_located_to_be_selected
15. element_selection_state_to_be
16. element_located_selection_state_to_be

最后一个条件判断一个元素是否仍在DOM中，传入WebElement对象，可以判断页面是否刷新了
17. staleness_of

======================================================================================
<<淘宝爬虫注意事项>>
如果直接使用WebDriver，不做任何修改的话，淘宝可以断定启动的浏览器是“机器人”，而不是“死的机器”。
如果想让淘宝错误地认为启动的浏览器是"死的机器"，那么就需要修改webdriver。
我使用的是chromedriver，"perl -pi -e 's/cdc_/dog_/g' /usr/local/bin/chromedriver"是修改chromedriver的代码，
直接在Terminal执行即可。执行完在运行脚本，则可以成功登录。
这里我解释一下"perl -pi -e 's/cdc_/dog_/g' /usr/local/bin/chromedriver"，
这段代码其实就是全局修改/usr/local/bin/chromedriver中的cdc_为dog_，"/usr/local/bin/chromedriver"是chromedriver所在的文件路径。
"""
# -*- coding:utf-8 -*-
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Spider(object):

    def __init__(self, url=''):
        self.source_url = url
        """
        chrome_options = webdriver.ChromeOptions()
        # 不加载图片，加快访问速度
        chrome_options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
        # 设置为开发者模式，避免被识别
        chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
        self.web_driver = webdriver.Chrome(options=chrome_options)
        """
        # 选择浏览器驱动
        self.driver = webdriver.Chrome()
        # 显示等待10秒
        self.waiting = WebDriverWait(self.driver, 10)
        # 隐示等待10秒
        self.driver.implicitly_wait(10)

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

    def open_new_windows(self, new_url=''):
        """
        打开一个新的windows窗口
        :param new_url: 新的URL
        :return:
        """
        js = "window.open({})".format(new_url)
        self.driver.execute_script(js)
        time.sleep(2)

    def page_scrolling(self, go_to_bottom=False, rolling_distance=(0, 1000)):
        """
        页面滚动，如果没有滚动效果，添加延时（页面需要全部加载完毕才能滚动）
        :param bool go_to_bottom: 默认为False，如果为True则滚动到当前页面的最底部
        :param tuple rolling_distance: 滚动距离，默认是向下滚动1000像素
        :return:
        """
        time.sleep(5)
        if go_to_bottom:
            js = "window.scrollTo(0, document.body.scrollHeight)"
        else:
            js = "window.scrollBy({}, {})".format(rolling_distance[0], rolling_distance[1])
        self.driver.execute_script(js)
        time.sleep(1)

    def screen_shot(self, picture_name='example.jpg'):
        """
        截取当前网页并保存为图片
        :param picture_name: 图片名称
        :return:
        """
        self.driver.save_screenshot(picture_name)

    def close_current_windows(self):
        # 关闭当前页面
        if self.driver:
            self.driver.close()

    def quit_browser(self):
        # 退出所有页面
        if self.driver:
            self.driver.quit()

    def main(self):
        # 打开网页
        self.driver.get(self.source_url)
        # TODO 普通定位
        # enter = self.driver.find_element_by_xpath('//*[@id="kw"]')

        # 通过验证元素是否出现定位
        enter = self.waiting.until(EC.presence_of_element_located((By.XPATH, '//*[@id="kw"]')))
        # 模拟输入文本
        enter.send_keys('python')
        # 执行输入
        enter.send_keys(Keys.ENTER)
        # 滚动页面
        self.page_scrolling()
        # 获取网页html
        html = self.driver.page_source
        print('found html:\n', html)


if __name__ == '__main__':
    spider = Spider(url='https://www.baidu.com')
    spider.main()
