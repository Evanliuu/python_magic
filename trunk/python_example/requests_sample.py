import re
import requests
from requests.exceptions import ReadTimeout, ConnectionError, RequestException
from fake_useragent import UserAgent
from requests.auth import HTTPBasicAuth

GET = 'get'
POST = 'post'


class Crawler(object):

    def __init__(self, url=''):
        self.base_url = url

    def get_web_page(self, url=None, purpose=GET):
        url = url or self.base_url
        # TODO 使用随机请求头
        # ua = UserAgent(use_cache_server=False)
        # headers = {'User-Agent': ua.random}
        headers = {
            # 使用谷歌浏览器请求头
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36'
        }
        params = {
            # 请求体内容
            "wd": 'python'
        }
        # TODO 使用代理突破限制IP访问频率
        # proxies = {
        #     "http": "http://10.10.1.10:3128",
        #     "https": "http://10.10.1.10:1080",
        # }
        try:
            # TODO 使用Session保持会话状态
            # s = requests.Session()
            # response = requests.get(url)
            # TODO 登陆网站时需要输入账户密码则调用auth参数传入即可
            # response = requests.get(url, auth=HTTPBasicAuth('username', 'password'))
            if purpose == GET:
                response = requests.get(url, headers=headers, params=params, timeout=5)
            else:
                response = requests.post(url, headers=headers, data=params, timeout=5)

            if response.status_code == 200:
                return response
                # response.text # 网页源码 [type: str]
                # response.headers # 头部信息 [type: dict]
                # response.json() # json格式 [type: json]
                # response.content # 二进制数据 [type: bytes]
                # response.cookies # 网页cookies [type: dict]
                # response.history # 访问的历史记录 [type: list]
            else:
                return None
        except ReadTimeout:  # 访问超时错误
            print('the url ({}) Time out'.format(url))
            return None
        except ConnectionError:  # 网络连接中断错误
            print('the url ({}) Connect error'.format(url))
            return None
        except RequestException:  # 父类错误
            print('the url ({}) Error'.format(url))
            return None

    @staticmethod
    def find_url(msg=''):
        regex = re.compile('[a-zA-Z]+://\S*')
        result = re.findall(regex, msg)
        print('find url:\n', result)
        print('find down, total url: {}'.format(len(result)))
        return result

    @staticmethod
    def main():
        source = crawler.get_web_page(purpose=GET)
        if source:
            # 筛选出网页里的url
            crawler.find_url(source.text)


if __name__ == '__main__':
    crawler = Crawler(url='https://www.baidu.com')
    crawler.main()
