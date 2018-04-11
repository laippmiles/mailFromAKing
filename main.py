from datetime import datetime
from sendEmailFromLzy import  mailFromLZY
from getSubAndCon import getSubAndCon
from random import uniform
from time import sleep
#说明：大致框架来自百度，不懂的可以微博私信问我。我有空回。
#微博:miles_corgi
def mail(hour,h):
    subject, content = getSubAndCon(hour,h)
    fileName = 'file0.jpg'
    filePath = r'D:\桌面\mailFromAKing\file' + '\\'
    #实际上这套代码是可以带附件的，不过没怎么用过，调通就放那不动了
    mailFromLZY(subject, content,hour,h, filePath, fileName, sendFile=False)
    #sendFile=False的时候不会发送附件


def main():
    '''h表示设定的小时，m为设定的分钟'''
    print('Begin')
    h = [8, 14, 23]
    index = int(uniform(0,len(h)))
    mailtime = h[index]
    m = int(uniform(1,59))#赋初值
    #m=20
    print('Init m：',m)
    #print(m)
    # 判断是否达到设定时间，例如0:00
    while True:
        while True:
            #内部死循环是为了检测时间的
            now = datetime.now()
            if now.hour == 1 and now.minute == 13:
                index = int(uniform(0,len(h)))
                mailtime = h[index]
                print('Update mailtime:',mailtime)
            if now.hour not in  h:
                m = int(uniform(1, 59)) #只在非发信时段更新m值    
            if now.hour == mailtime and now.minute == m:
                break# 到达设定时间，结束内循环
            sleep(30)#检测周期是30秒
            print('Now Time：',now.hour,'：',now.minute,'：',now.second)
            print('Update m：',m,'Today mail time :', mailtime)
        # 到点发信
        mail(now.hour,h)
        sleep(60)
        # 等60秒，到下一分钟再开检测
main()
