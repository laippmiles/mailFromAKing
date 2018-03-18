#!/usr/bin/python
# -*- coding: UTF-8 -*-
import smtplib
import email.mime.multipart
import email.mime.text
from passWord import decode
from email.mime.application import MIMEApplication
from email.utils import formataddr
from time import sleep
from getTo import getTo

def sendEmailFromLzy(subject, content , filePath= r'D:\桌面\mailFromAKing\file' + '\\', fileName= 'file0.jpg',sendFile = False):
    import smtplib
    import os
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    #from email import encoders
    msg = email.mime.multipart.MIMEMultipart()
    user = decode(113,'E9C8@8F:A9<889;8<8@99;?9F9A8D989@9E9G=:9F9D9')
    pwd = decode(113,'88@8B9=8G988A9C9:9@9D9C9=989@9;9')

    msg['From'] = formataddr(["李泽言", user])

    msg['Subject'] = subject
    content1 = MIMEText(content, 'plain', 'utf-8')
    msg.attach(content1)
    if sendFile == True:
    #------------------------------------------------------------
        annexPath = filePath + fileName
        part = MIMEApplication(open(annexPath,'rb').read())
        part.add_header('Content-Disposition', 'attachment', filename= fileName)
        msg.attach(part)
    # -----------------------------------------------------------
    smtpHost = decode(422, '=UCT:U>U@P?U?U@P=TATCT')
    s = smtplib.SMTP_SSL(smtpHost,465)
    s.login(user, pwd)

    toList = getTo()
    for to  in toList:
        msg['to'] = to
        s.sendmail(user, to, msg.as_string())
        print('发送成功')
        sleep(3)
        #每隔3秒发一次信
    s.close()


def mailFromLZY(subject, content, filePath, fileName, sendFile = False):
    try:
        sendEmailFromLzy(subject, content, filePath, fileName,sendFile)
    except Exception as err:
        print(err)