import random
import requests


class Crawler(object):

    def __init__(self, url=None):
        self.source_url = url

    @staticmethod
    def random_headers():
        ua_list = [
            # Chrome UA
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
            ' Chrome/73.0.3683.75 Safari/537.36',
            # IE UA
            'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
            # Microsoft Edge UA
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
            ' Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763'
        ]
        ua = random.choice(ua_list)
        return ua

    def get_web_page(self, request_url=None):
        """
        请求网页数据并返回响应结果
        :param request_url: 请求的URL
        :return:
        """
        request_url = request_url or self.source_url
        headers = {
            "User-Agent": self.random_headers(),
        }
        try:
            response = requests.get(request_url, headers=headers, timeout=60)
            if response.status_code == 200:
                return response
        except Exception as ex:
            print('Get web page error: {}'.format(ex))
            return None


def main():
    resource_url = 'https://www.jianshu.com/'
    crawler = Crawler(url=resource_url)

    response = crawler.get_web_page()
    if response:
        print('Response:\n{}'.format(response.text))


if __name__ == '__main__':
    main()
