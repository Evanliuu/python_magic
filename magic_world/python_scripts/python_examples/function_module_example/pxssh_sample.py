from pexpect import pxssh
import getpass


def run():
    try:
        # TODO pxssh功能只能在Linux端使用
        s = pxssh.pxssh()
        hostname = input('hostname: ')
        username = input('username: ')
        password = input('password: ')
        # password = getpass.getpass('password: ')  # pycharm中无法使用此功能

        # 利用 login 方法进行 ssh 登录，初始 prompt 为'$' , '#'或'>'
        s.login(hostname, username, password, original_prompt='[$#>]')
        # 发送命令
        s.sendline('ls -l')
        # 匹配 prompt
        s.prompt()
        # 将 prompt 前所有内容打印出，即命令 ' ls -l ' 的执行结果.
        print(s.before)
        # 退出 ssh session
        s.logout()
    except pxssh.ExceptionPxssh as ex:
        print('ssh error, error msg: {}'.format(ex))


if __name__ == '__main__':
    run()
