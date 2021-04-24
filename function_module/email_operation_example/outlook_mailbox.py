import os
from win32com import client as win32  # 发送邮件模块
from win32com.client.gencache import EnsureDispatch as Dispatch  # 读取邮件模块

__author__ = 'Evan'


def read_outlook_mailbox():
    """连接Outlook邮箱，读取收件箱内的邮件内容"""
    # 使用MAPI协议连接Outlook
    account = Dispatch('Outlook.Application').GetNamespace('MAPI')

    # 获取收件箱所在位置
    inbox = account.GetDefaultFolder(6)  # 数字6代表收件箱
    # 获取收件箱下的所有邮件
    mails = inbox.Items
    mails.Sort('[ReceivedTime]', True)  # 邮件按时间排序

    # 读取收件箱内前3封邮件的所有信息（下标从1开始）
    for index in range(1, 4):
        print('正在读取第[{}]封邮件...'.format(index))
        mail = mails.Item(index)
        print('接收时间：{}'.format(str(mail.ReceivedTime)[:-6]))
        print('发件人：{}'.format(mail.SenderName))
        print('收件人：{}'.format(mail.To))
        print('抄送人：{}'.format(mail.CC))
        print('主题：{}'.format(mail.Subject))
        print('邮件正文内容：{}'.format(mail.Body))
        print('邮件附件数量：{}'.format(mail.Attachments.Count))
        print('邮件MessageID：{}'.format(mail.EntryID))
        print('会话主题：{}'.format(mail.ConversationTopic))
        print('会话ID：{}'.format(mail.ConversationID))
        print('会话记录相对位置：{}'.format(mail.ConversationIndex))

        # 保存邮件中的附件，如果没有附件不会执行也不会产生异常
        attachment = mail.Attachments
        for each in attachment:
            save_attachment_path = os.getcwd()  # 保存附件到当前路径
            each.SaveAsFile(r'{}\{}'.format(save_attachment_path, each.FileName))
            print('附件（{}）保存完毕'.format(each.FileName))


def send_mail():
    """
    连接Outlook邮箱，发送邮件
    :return:
    """
    outlook = win32.Dispatch('Outlook.Application')  # 连接Outlook

    mail_item = outlook.CreateItem(0)  # 创建新邮件
    mail_item.Recipients.Add('test@test.com')  # 收件人邮箱
    mail_item.Subject = 'Mail Test'  # 主题
    mail_item.BodyFormat = 2  # 使用HTML格式编写正文
    mail_item.HTMLBody = """"
    <H2>Hello, This is a test mail.</H2>
    Hello World.
    """
    # mail_item.Attachments.Add('test.csv')  # 添加附件
    mail_item.Send()  # 发送邮件


if __name__ == '__main__':
    read_outlook_mailbox()
    send_mail()
