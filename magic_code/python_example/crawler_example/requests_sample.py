import random
import requests
from requests.exceptions import ReadTimeout, ConnectionError, RequestException
from urllib.parse import urljoin, quote

GET = 'get'
POST = 'post'


class Crawler(object):

    def __init__(self, base_url=None):
        self.base_url = base_url

    @staticmethod
    def random_headers():
        ua_list = [
            # Chrome UA
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36',
            # IE UA
            'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
            # Microsoft Edge UA
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763'
        ]
        ua = random.choice(ua_list)
        headers = {'User-Agent': ua}
        return headers

    def get_web_page(self, url=None, purpose=GET):
        """ Request example：
        1:
        使用随机请求头:
            from fake_useragent import UserAgent
            ua = UserAgent(use_cache_server=False)
            headers = {'User-Agent': ua.random}
            or
            headers = self.random_headers()
        2:
        使用带请求参数的request：
            GET: params = {"wd": 'python'}
            POST: data = {"wd": 'python'}
        3:
        使用代理突破限制IP访问频率:
            proxies = {
                "http": "http://10.10.1.10:3128",
                "https": "http://10.10.1.10:1080",
            }
        4:
        使用Session保持会话状态：
            s = requests.Session()
            response = s.get(url)
        5:
        登陆网站时需要输入账户密码则调用auth参数传入即可:
            from requests.auth import HTTPBasicAuth
            response = requests.get(url, auth=HTTPBasicAuth('username', 'password'))
        """
        url = url or self.base_url
        headers = {
            # 使用谷歌浏览器请求头
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36'
        }
        try:
            if purpose == GET:
                response = requests.get(url, headers=headers, timeout=60)
            else:
                response = requests.post(url, headers=headers, timeout=60)

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
    def main():
        # 中文转换字节码
        # like = quote('你好')
        # print(like)

        # 获取网页内容
        source = crawler.get_web_page(purpose=GET)
        if source:
            with open('beautiful.jpg', 'wb') as file:
                file.write(source.content)


if __name__ == '__main__':
    base_url = 'http://img.netbian.com/file/2019/0418/92a06dd21f1a38d97c930ce3e11b4123.jpg'
    crawler = Crawler(base_url=base_url)
    crawler.main()
