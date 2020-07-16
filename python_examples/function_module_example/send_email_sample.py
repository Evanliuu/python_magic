"""电子邮件发送模块使用方法（email，smtplib）
===============================配置邮件正文模块===============================
email用法：
from email.mime.text import MIMEText  # 文本邮件对象（构造普通文本、超文本、文本附件）
from email.mime.image import MIMEImage  # 图片对象（构造图片附件）
from email.mime.multipart import MIMEMultipart  # 容器对象（构造一个容器，可以添加文本也可以添加附件）

-------------------------------使用MIMEText对象-------------------------------
# 构造普通文本
text_info = 'Hello Evan'
text_obj = MIMEText(text_info, 'plain', 'utf-8')  # 第一个参数文本信息，第二个参数文本格式，第三个参数编码格式
text_obj["Content-Disposition"] = 'attachment;filename="hello.txt"'  # 如果要添加为附件就一定要配置这行，否则会视为普通文本

# 构造超文本附件
html_info = '<p>Hello Evan</p>'
html_obj = MIMEText(html_info, 'html', 'utf-8')  # 第一个参数超文本信息，第二个参数超文本格式，第三个参数编码格式
html_obj["Content-Disposition"] = 'attachment;filename="hello.html"'

# 构造base64数据流附件，用于发送文件的时候使用
txt_file = open('file_path', 'rb').read()
txt_obj = MIMEText(txt_file, 'base64', 'utf-8')
txt_obj["Content-Disposition"] = 'attachment;filename="hi.txt"'

-------------------------------使用MIMEImage对象-------------------------------
# 构造图片附件
image_file = open('image_path', 'rb').read()
image_obj = MIMEImage(image_file)
image_obj["Content-Disposition"] = 'attachment;filename="image.png"'

-------------------------------使用MIMEMultipart对象-------------------------------
MIMEMultipart实例化有三个可选类型，分别为:
* alternative: 邮件正文中包含纯文本正文（text/plain）和超文本正文（text/html）
* related: 邮件正文中包含图片，声音等内嵌资源
* mixed: 邮件包含附件，图片，文本等（默认为这个，选择mixed类型什么都可以发）

multipart_obj = MIMEMultipart('mixed')
multipart_obj['subject'] = Header('Hello Evan’, 'utf-8')  # 配置邮件主题
multipart_obj['From'] = '777@qq.com'  # 配置发件方邮箱
multipart_obj['To'] = '666@qq.com'  # 配置发件方邮箱
multipart_obj.attach(ready_obj)  # 添加构造好的文本对象或者附件对象（txt_obj、image_obj、html_obj）

===============================发送邮件模块===============================
smtplib用法：
import smtplib

receiver_mail = '666@qq.com'  # 接收方的邮箱地址，可以是一个字符串，也可以是一个列表（列表包含所有邮箱地址的字符串）
sender_mail='777@qq.com' # 发送方的邮箱地址
auth_code = 'abc' # 发送方邮箱提供的第三方登录授权码（如QQ邮箱：设置-账户-开启服务-开启POP3/SMTP服务，然后点击生成授权码）

sftp_obj = smtplib.SMTP('smtp.qq.com', 25)  # 实例化SMTP对象，端口号为25
sftp_obj.login(sender_mail, auth_code)  # 使用发送方邮箱账号和第三方登录授权码模拟登录

send_message = ready_obj  # 构造好的文本对象或者附件对象（txt_obj、image_obj、html_obj、multipart_obj）
sftp_obj.sendmail(sender_mail, receiver_mail, send_message.as_string())  # 发送邮件
sftp_obj.close()  # 关闭邮件发送客户端
"""
# -*- coding:utf-8 -*-
import smtplib

from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

__author__ = 'Evan'


def send_email(sender_email, receive_email, auth_code):
    """
    发送电子邮件
    :param sender_email: 发件邮箱
    :param receive_email: 收件邮箱，可以是一个字符串，也可以是一个列表（列表包含所有邮箱地址的字符串）
    :param auth_code: 发件邮箱的授权登录密码
    :return:
    """
    # 实例化容器对象
    send_obj = MIMEMultipart('mixed')
    send_obj['From'] = 'Evan Liu'
    send_obj['To'] = receive_email
    send_obj['subject'] = Header('This is a test', 'utf-8')

    # 构造文本内容附件
    text_info = 'Hello Evan'
    text_obj = MIMEText(text_info, 'plain', 'utf-8')
    text_obj["Content-Disposition"] = 'attachment;filename="test.txt"'
    send_obj.attach(text_obj)

    # 模拟登录邮箱
    sftp_obj = smtplib.SMTP('smtp.qq.com', 25)
    sftp_obj.login(sender_email, auth_code)

    # 发送邮件
    sftp_obj.sendmail(sender_email, receive_email, send_obj.as_string())
    sftp_obj.close()
    print('发送邮件到（{}）成功'.format(receive_email))


if __name__ == '__main__':
    send_email(sender_email='**@qq.com', receive_email='***@qq.com', auth_code='Enter your pass code')
