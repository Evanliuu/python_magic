"""电子邮件模块使用方法

配置邮件正文模块：
    from email.mime.text import MIMEText  # 文本邮件对象（构造普通文本、超文本、文本附件）
    from email.mime.image import MIMEImage  # 图片对象（构造图片附件）
    from email.mime.multipart import MIMEMultipart  # 容器对象（构造一个容器，可以添加文本也可以添加附件）

    使用MIMEText对象：
        1. 构造普通文本内容
        text_info = 'Hello Evan'
        text_obj = MIMEText(text_info, 'plain', 'utf-8')  # 第一个参数文本信息，第二个参数文本格式，第三个参数编码格式

        2. 构造超文本内容
        html_info = '<p>Hello Evan</p>'
        html_obj = MIMEText(html_info, 'html', 'utf-8')  # 第一个参数超文本信息，第二个参数超文本格式，第三个参数编码格式

        3. 构造base64数据流附件，用于发送文件的时候使用
        file_path = 'example.txt'
        txt_file = open(file_path, 'rb')
        file_obj = MIMEText(txt_file.read(), 'base64', 'utf-8')
        txt_file.close()
        file_obj["Content-Type"] = 'application/octet-stream'
        file_obj["Content-Disposition"] = 'attachment;filename="{}"'.format(Header(os.path.basename(file_path).encode('utf-8'), 'utf-8'))

    使用MIMEImage对象（构造图片附件）：
        file_path = 'example.txt'
        image_file = open(file_path, 'rb')
        image_obj = MIMEImage(image_file.read())
        image_file.close()
        image_obj["Content-Type"] = 'application/octet-stream'
        image_obj["Content-Disposition"] = 'attachment;filename="{}"'.format(Header(os.path.basename(file_path).encode('utf-8'), 'utf-8'))

    使用MIMEMultipart对象：
        MIMEMultipart实例化有三个可选类型，分别为:
        * alternative: 邮件正文中包含纯文本正文（text/plain）和超文本正文（text/html）
        * related: 邮件正文中包含图片，声音等内嵌资源
        * mixed: 邮件包含附件，图片，文本等（默认为这个，选择mixed类型什么都可以发）

        multipart_obj = MIMEMultipart('mixed')
        multipart_obj['subject'] = Header('Hello Evan’, 'utf-8')  # 配置邮件主题
        multipart_obj['From'] = '777@qq.com'  # 配置发件方邮箱
        multipart_obj['To'] = '666@qq.com'  # 配置发件方邮箱
        multipart_obj.attach(ready_obj)  # 添加构造好的文本对象或者附件对象（txt_obj、image_obj、html_obj）

发送邮件模块（使用QQ邮箱例子）：
    import smtplib

    receiver_mail = '666@qq.com'  # 接收方的邮箱地址
    sender_mail='777@qq.com' # 发送方的邮箱地址
    auth_code = 'abc' # 发送方邮箱提供的第三方登录授权码（如QQ邮箱：设置-账户-开启服务-开启POP3/SMTP服务，然后点击生成授权码）

    sftp_obj = smtplib.SMTP('smtp.qq.com', 25)  # 实例化SMTP对象，端口号为25
    sftp_obj.login(sender_mail, auth_code)  # 使用发送方邮箱账号和第三方登录授权码模拟登录

    send_message = ready_obj  # 构造好的文本对象或者附件对象（txt_obj、image_obj、html_obj、multipart_obj）
    sftp_obj.sendmail(sender_mail, receiver_mail, send_message.as_string())  # 发送邮件
    sftp_obj.quit()  # 退出登陆
"""
# -*- coding:utf-8 -*-
import smtplib

from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

__author__ = 'Evan'


def send_email(sender, receiver, auth_code, subject='This is a test'):
    """
    发送电子邮件
    :param sender: 发件邮箱
    :param receiver: 收件邮箱
    :param auth_code: 发件邮箱的授权登录密码
    :param subject: 邮件主题
    :return:
    """
    # 实例化容器对象
    send_obj = MIMEMultipart('mixed')
    send_obj['From'] = 'Evan Liu'
    send_obj['To'] = ','.join(receiver)  # 将所有的接收邮箱转成字符串，用逗号隔开
    send_obj['subject'] = Header(subject, 'utf-8')

    # 构造普通文本内容
    text_info = 'Hello Evan'
    text_obj = MIMEText(text_info, 'plain', 'utf-8')
    send_obj.attach(text_obj)

    # 构造超文本内容
    # text_info = '<p> Hello Evan </p>'
    # html_obj = MIMEText(text_info, 'html', 'utf-8')
    # send_obj.attach(html_obj)

    # 构造附件
    # file_path = 'example.txt'
    # txt_file = open(file_path, 'rb')
    # file_obj = MIMEText(txt_file.read(), 'base64', 'utf-8')
    # txt_file.close()
    # file_obj["Content-Type"] = 'application/octet-stream'
    # file_obj["Content-Disposition"] = 'attachment;filename="{}"'\
    #     .format(Header(os.path.basename(file_path).encode('utf-8'), 'utf-8'))
    # send_obj.attach(file_obj)

    # 使用服务器登陆
    # sftp_obj = smtplib.SMTP('smtp_server_ip', 'server_port')
    # sftp_obj.connect(host='smtp_server_ip', port='server_port')
    # sftp_obj.login(user=sender, password=auth_code)

    # 使用QQ邮箱登陆
    sftp_obj = smtplib.SMTP('smtp.qq.com', 25)
    sftp_obj.login(user=sender, password=auth_code)

    # 发送邮件
    sftp_obj.sendmail(sender, receiver, send_obj.as_string())
    print('发送邮件到（{}）成功'.format(receiver))

    # 退出登陆
    sftp_obj.quit()


if __name__ == '__main__':
    send_email(sender='**@qq.com', receiver=['**@qq.com'], auth_code='Enter your pass code')
