# -*- coding:utf-8 -*-


def calculate(money):
    """
    有一个贩卖机，1元可以买一瓶酒，2个空瓶可以换一瓶酒，我有20元钱，最多可以喝到多少瓶酒？
    :param money:
    :return:
    """
    exchange = money // 2  # 用空瓶交易后的啤酒数量
    remainder = money % 2  # 剩下不能交易的空瓶子

    if (exchange + remainder) <= 1:
        return exchange + remainder  # 返回最后一次喝的酒

    return money + calculate(exchange + remainder)


if __name__ == '__main__':
    print(calculate(money=20))
