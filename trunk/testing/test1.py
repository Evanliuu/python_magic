# -*- coding:utf-8 -*-
import re
import random
import requests
import xlwt

from bs4 import BeautifulSoup
from urllib.parse import unquote


class Crawler(object):

    def __init__(self, url=''):
        self.source_url = url

    @staticmethod
    def random_user_agent():
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

    @staticmethod
    def write_excel_table(write_info, table_name='excel_example.xls'):
        """
        写入Excel表格
        :param write_info: 要写入Excel表格的数据
        :param table_name: Excel表格名称
        :return:
        """
        ex_wt = xlwt.Workbook()

        for i in write_info:
            title = i[0]
            body = i[1]
            sheet1 = ex_wt.add_sheet(title, cell_overwrite_ok=True)

            for row_index, each_row in enumerate(body.splitlines()):
                if isinstance(each_row, (list, tuple)):
                    # 如果是列表或者元组，循环写入每条数据
                    for column_index, each_column in enumerate(each_row):
                        sheet1.write(row_index, column_index, each_column)
                else:
                    # 写入一条数据
                    sheet1.write(row_index, 0, each_row)
        ex_wt.save(table_name)

    def parse(self, parse_url, note_id):
        resp = requests.get(parse_url, headers={'User-Agent': self.random_user_agent()})
        result = []
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.text, 'lxml')
            content = soup.find('div', id='note-{}'.format(note_id))
            title = content.find('div', class_='note-header note-header-container').find('h1').text
            body = content.find('div', id='note_{}_full'.format(note_id)).text
            for info in [title, body]:
                result.append(str(info).strip())
        return result

    def start_search(self, params):
        resp = requests.get(self.source_url, headers={'User-Agent': self.random_user_agent()}, params=params)
        result = []
        if resp.status_code == 200:
            for i in resp.json()['items']:
                if params['q'] in str(i):
                    url_info = re.search('a href="(.+?)"', i)
                    if url_info:
                        result.append(url_info.group(1))
        return result


if __name__ == '__main__':
    crawler = Crawler(url='https://www.douban.com/j/search')

    loops = 1
    final_list = []
    start_increment = 5
    while True:
        print('loops: {}'.format(loops))
        print('final_list length: {}'.format(len(final_list)))

        if len(final_list) >= 5:
            # TODO Wait for change
            Crawler.write_excel_table(write_info=final_list, table_name='DouBan.xls')
            print('Write excel table successful')
            break

        data = {
            'q': '唇炎',
            'start': start_increment,
            'cat': 1015
        }
        url_list = crawler.start_search(params=data)
        if url_list:
            print('Found url list length: {}'.format(len(url_list)))

            parsed_info = []
            for url in url_list:
                note = re.search('note/(.+?)/&amp', unquote(url))
                if id:
                    contents = crawler.parse(parse_url=url, note_id=note.group(1))
                    if contents:
                        parsed_info.append(contents)

            print('parsed_info length: {}'.format(len(parsed_info)))
            final_list.extend(parsed_info)
            print('url list pares done')

        start_increment += 20
        loops += 1
        print('current start_increment value: {}\n----------------------------\n'.format(start_increment))
