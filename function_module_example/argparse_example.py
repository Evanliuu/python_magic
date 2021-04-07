import sys
import argparse
import ipaddress


# 使用sys获取所有的输入参数
print(f'当前文件路径: {sys.argv[0]}')
print(f'所有的输入参数：{sys.argv[1:]}')


def check_ip(ip):
    """
    检查输入的ip是否符合规范
    :param ip:
    :return:
    """
    try:
        ipaddress.ip_address(ip)
    except Exception:
        msg = "Invalid IP Address: '{0}'.".format(ip)
        raise argparse.ArgumentTypeError(msg)
    return ip


# 定义命令行参数（type：检查函数，required：是否必须）
parser = argparse.ArgumentParser(description='argument example')
parser.add_argument("-ip", "--ip", type=check_ip, help="请填入主机IP，例如：-ip 192.168.xx.xx", required=True)

# 使用parse_args获取输入值
args = parser.parse_args()
print(f'获取ip值：{args.ip}')
