"""<<WebDriver模块12个常用方法>>
模块方法:                                含义:
1.  set_window_size()	                设置浏览器的大小
2.  back()	                            控制浏览器后退
3.  forward()	                        控制浏览器前进
4.  refresh()	                        刷新当前页面
5.  clear()	                            清除文本
6.  send_keys (value)	                模拟按键输入
7.  click()	                            单击元素
8.  submit()	                        用于提交表单
9.  get_attribute(name)	                获取元素属性值
10. is_displayed()	                    设置该元素是否用户可见
11. size	                            返回元素的尺寸
12. text	                            获取元素的文本

<<定位元素>>
定位一个元素:                             定位多个元素:                              含义:
1. find_element_by_id	                 find_elements_by_id	                  通过元素id定位
2. find_element_by_name	                 find_elements_by_name	                  通过元素name定位
3. find_element_by_xpath	             find_elements_by_xpath	                  通过xpath表达式定位
4. find_element_by_link_text	         find_elements_by_link_tex	              通过完整超链接定位
5. find_element_by_partial_link_text	 find_elements_by_partial_link_text	      通过部分链接定位
6. find_element_by_tag_name	             find_elements_by_tag_name	              通过标签定位
7. find_element_by_class_name	         find_elements_by_class_name	          通过类名进行定位
8. find_elements_by_css_selector	     find_elements_by_css_selector	          通过css选择器进行定位

<<等待条件函数>>
等待条件:                                            含义:
1.  title_is                                        标题是某内容
2.  title_contains                                  标题包含某内容
3.  presence_of_element_located                     节点加载出来，传入定位元组，如（By.ID, 'p'）
4.  presence_of_all_elements_located                所有节点加载出来
5.  visibility_of_element_located                   节点可见，传入定位元组
6.  visibility_of                                   可见，传入节点对象
7.  text_to_be_present_in_element                   某个节点文本包含某文字
8.  text_to_be_present_in_element_value             某个节点值包含某文字
9.  frame_to_be_available_and_switch_to_it          加载并切换
10. invisibility_of_element_located                 节点不可见
11. alert_is_present                                是否出现警告
12. element_to_be_clickable                         节点可点击
13. element_to_be_selected                          节点可选择，传入节点对象
14. element_located_to_be_selected                  节点可选择，传入定位元组
15. element_selection_state_to_be                   传入节点对象以及状态，相等返回True，否则返回False
16. element_located_selection_state_to_be           传入定位元组以及状态，相等返回True，否则返回False
17. staleness_of                                    判断一个节点是否仍在DOM，可判断当前页面是否已经刷新

======================================================================================
<<淘宝爬虫注意事项>>
如果直接使用WebDriver，不做任何修改的话，淘宝可以断定启动的浏览器是“机器人”，而不是“死的机器”。
如果想让淘宝错误地认为启动的浏览器是"死的机器"，那么就需要修改webdriver。
我使用的是chromedriver，"perl -pi -e 's/cdc_/dog_/g' /usr/local/bin/chromedriver"是修改chromedriver的代码，
直接在Terminal执行即可。执行完在运行脚本，则可以成功登录。
这里解释一下"perl -pi -e 's/cdc_/dog_/g' /usr/local/bin/chromedriver"，
这段代码其实就是全局修改/usr/local/bin/chromedriver中的cdc_为dog_，"/usr/local/bin/chromedriver"是chromedriver所在的文件路径。
"""
# -*- coding:utf-8 -*-
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Crawler(object):

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
        self.driver = webdriver.Chrome()  # 选择浏览器驱动
        self.waiting = WebDriverWait(self.driver, 30)  # 设置显示等待30秒
        self.driver.implicitly_wait(30)  # 设置隐示等待30秒
        self.actions = webdriver.ActionChains(self.driver)  # 动作链初始化

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
        :param index: expect by frame index value or id or name or element
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

    def screen_shot(self, picture_name='example.jpg'):
        """
        截取当前网页并保存为图片
        :param picture_name: 保存的图片名称
        :return:
        """
        self.driver.save_screenshot(picture_name)

    def action_chain(self, source, target):
        """
        执行鼠标拖曳
        :param source: 拖曳前位置
        :param target: 拖曳后位置
        :return:
        """
        self.actions.drag_and_drop(source, target)
        self.actions.perform()

    def close_current_windows(self):
        # 关闭当前页面
        if self.driver:
            self.driver.close()

    def quit_browser(self):
        # 退出所有页面
        if self.driver:
            self.driver.quit()

    def main(self):
        # 访问页面
        self.driver.get(self.source_url)

        # 定位节点
        self.driver.find_element_by_xpath('//*[@id="kw"]')  # 通过xpath定位
        input_box = self.waiting.until(EC.presence_of_element_located((By.XPATH, '//*[@id="kw"]')))  # 通过等待条件定位

        # 获取节点信息
        print(input_box.get_attribute('class'))  # 获取节点的class属性值
        print(input_box.id)  # 获取节点的id值
        print(input_box.text)  # 获取节点的文本值
        print(input_box.location)  # 获取节点在页面中的相对位置
        print(input_box.tag_name)  # 获取节点的标签名称
        print(input_box.size)  # 获取节点的大小
        # 获取网页信息
        print(self.driver.current_url)  # 获取当前的URL
        print(self.driver.get_cookies())  # 获取当前的Cookies
        print(self.driver.page_source)  # 获取网页源代码

        # 节点交互
        input_box.clear()  # 清空文本
        input_box.send_keys('python')  # 输入文本
        input_box.send_keys(Keys.ENTER)  # 执行输入
        # 网页交互
        self.driver.back()  # 网页后退
        time.sleep(1)
        self.driver.forward()  # 网页前进
        # 滚动页面
        self.page_scrolling()  # 执行javascript
        # 动作链
        source = self.driver.find_element_by_xpath('//*[@id="result_logo"]/img[1]')
        target = self.driver.find_element_by_xpath('//*[@id="kw"]')
        self.action_chain(source=source, target=target)  # 鼠标拖曳


if __name__ == '__main__':
    crawler = Crawler(url='https://www.baidu.com')
    crawler.main()
