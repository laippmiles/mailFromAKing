from datetime import datetime
from sendEmailFromLzy import  mailFromLZY
from getSubAndCon import getSubAndCon
from random import uniform
from time import sleep

def mail(hour,h):
    subject, content = getSubAndCon(hour,h)
    fileName = 'file0.jpg'
    filePath = r'D:\桌面\mailFromAKing\file' + '\\'
    mailFromLZY(subject, content,hour,h, filePath, fileName, sendFile=False)


def main():
    '''h表示设定的小时，m为设定的分钟'''
    print('Begin')
    h = [8, 14, 23]
    m = int(uniform(1,59))#赋初值
    print('Init m：',m)
    #print(m)
    # 判断是否达到设定时间，例如0:00
    while True:
        while True:
            #内部死循环是为了检测时间的
            now = datetime.now()
            if now.hour not in  h:
                m = int(uniform(1, 59)) #只在非发信时段更新m值    
            if now.hour in h and now.minute == m:
                break# 到达设定时间，结束内循环
            sleep(20)#检测周期是十秒
            print('Now Time：',now.hour,'：',now.minute,'：',now.second)
            print('Update m：',m)
        # 到点发信
        mail(now.hour,h)
        sleep(60)
        # 等60秒，到下一分钟再开检测
main()
