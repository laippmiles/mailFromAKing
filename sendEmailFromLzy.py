#!/usr/bin/python
# -*- coding: UTF-8 -*-
import smtplib
import email.mime.multipart
import email.mime.text
from email.mime.application import MIMEApplication
from email.utils import formataddr
from time import sleep
from getTo import getTo
from getSubAndCon import getSubAndCon

def sendEmailFromLzy(subject, content ,mailTime,h, filePath= r'D:\桌面\mailFromAKing\file' + '\\', fileName= 'file0.jpg',sendFile = False):
    import smtplib
    import os
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    #from email import encoders
    msg = email.mime.multipart.MIMEMultipart()
    user = '发信的邮箱，这套代码目前测试只有qq和Foxmail的邮箱能用，可以改一下邮箱名称让发信邮箱更李泽言'
    pwd = '发信邮箱的授权码，授权码获取方法自行百度'
    smtpHost = 'smtp.qq.com'
    s = smtplib.SMTP_SSL(smtpHost,465)
    s.login(user, pwd)

    toList = getTo()
    for to  in toList:
        subject, content = getSubAndCon(mailTime, h)
        msg = MIMEText(content, 'plain', 'utf-8')
        msg['From'] = formataddr(["李泽言", user])
        msg['Subject'] = subject
        msg['to'] = to
        if sendFile == True:
            # ------------------------------------------------------------
            annexPath = filePath + fileName
            part = MIMEApplication(open(annexPath, 'rb').read())
            part.add_header('Content-Disposition', 'attachment', filename=fileName)
            msg.attach(part)
        # -----------------------------------------------------------
        s.sendmail(user, to, msg.as_string())
        print('发送成功')
        sleep(3)
        #每隔3秒发一次信
    s.close()


def mailFromLZY(subject, content,hour,h, filePath, fileName, sendFile = False):
    try:
        sendEmailFromLzy(subject, content,hour,h, filePath, fileName,sendFile)
    except Exception as err:
        print(err)