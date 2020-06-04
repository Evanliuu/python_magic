# -*- coding:utf-8 -*-
import random

__author__ = 'Evan'


def get_random_red_envelope(all_money=100, count=15):
    """
    获取指定金额和数量的随机红包金额
    :param all_money: 金额总数
    :param count: 红包数量
    :return: 返回指定数量的随机红包金额
    """
    result = []  # 保存所有的随机红包金额
    total_money = all_money  # 金额总数
    for i in range(count-1):
        total_money = float('{:.2f}'.format(total_money))  # 转化为浮点数（保留两位小数）
        stage = total_money / 2
        money = float('{:.2f}'.format(random.uniform(0.01, stage)))  # 获取随机的金额
        total_money = total_money - money
        result.append(money)
    last_one_money = all_money - sum(result)  # 获取最后一个红包的金额
    result.append(float('{:.2f}'.format(last_one_money)))
    return result


if __name__ == '__main__':
    print(get_random_red_envelope(all_money=100, count=15))
    print(get_random_red_envelope(all_money=100, count=5))
    print(get_random_red_envelope(all_money=50, count=10))
