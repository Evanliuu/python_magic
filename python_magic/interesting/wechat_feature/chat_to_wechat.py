# -*- coding:utf-8 -*-
import itchat
import random
import time

__author__ = 'Evan'
blessing = ['春新猪似象，家和万事兴。新的一年，爆竹传吉语，腊梅报暖春；新的一年，天蓬增福寿，东风送吉祥。'
            '祝您猪年大吉，万事安康！',
            '犬问平安随冬去，猪拱财富贺春来。2019年，愿您猪岁新景满家园；2019年，愿您财源滚滚遍地开。新年好，给您拜年了！',
            ' 一年春为首，燕衔喜信春光好。六畜猪当先，四季平安添如意。君可见，玉犬献瑞吉庆多多，'
            '君可见，金猪报祥财源滚滚；君可见，千里春光美如画，君可见，五谷丰登旺财源。君可见金猪呈祥，家家乐，'
            '君可见玉犬鸣福户户欢！猪年行大运，腾跃吉祥年！',
            '成业立志，欢天喜地送玉犬，鸿图大展，张灯结彩迎金猪。愿您瑞气盈门，事事如意，祝您欢笑遍地，岁岁吉祥。'
            '新的一年，狗绘韵香喜报福音、猪描大地乐添春意。新的一年，犬岁荣耀增辉日月、猪年永照添好春光。'
            '2019，玉犬献礼，愿您合家顺利，金猪闹春，愿您万事大吉。']


@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    if ('祝' in msg.text) | ('福' in msg.text) | ('猪' in msg.text) | ('快乐' in msg.text) | ('年' in msg.text):
        index = random.randint(0, 3)
        time.sleep(3)
        return blessing[index]


def sending():
    want_to_say = u'祝%s开心快乐每一天'
    # 获取好友列表
    friend_list = itchat.get_friends(update=True)[1:]
    for friend in friend_list:
        print('friend: {}'.format(friend))
        # print('祝福语：', WANT_TO_SAY % (friend['DisplayName'] or friend['NickName']))
        itchat.send(want_to_say % (friend['DisplayName']or friend['NickName']), friend['UserName'])
        time.sleep(3)


if __name__ == "__main__":
    itchat.auto_login()
    sending()
    # itchat.run()
