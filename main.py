from datetime import datetime
from sendEmailFromLzy import  mailFromLZY
from getSubAndCon import getSubAndCon
from random import uniform
from time import sleep

def mail(h):
    subject, content = getSubAndCon(h)
    fileName = 'file0.jpg'
    filePath = r'D:\桌面\mailFromAKing\file' + '\\'
    mailFromLZY(subject, content, filePath, fileName, sendFile=False)


def main():

    '''h表示设定的小时，m为设定的分钟'''
    print('Begin')
    h = [8, 14, 20]
    m = int(uniform(0,59))#赋初值
    print('Init m：',m)
    #print(m)
    # 判断是否达到设定时间，例如0:00
    while True:
        while True:
            #内部死循环是为了检测时间的
            now = datetime.now()
            # 到达设定时间，结束内循环
            if now.hour in h and now.minute==m:
                break
            sleep(10)#检测周期是十秒
            print('Now Time：',now.hour,'：',now.minute,'：',now.second)
        # 做正事，一天做一次
        mail(now.hour)
        m = int(uniform(0, 59))#重设分钟数，要不达不到随机目的的
        print('Update m：', m)
        sleep(60)
        # 等60秒，到下一分钟再开检测
main()

