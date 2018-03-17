from sendEmailFromLzy import  mailFromLZY
#写文件名要用的
subject = '笨蛋'
content = '我想和你说Helloworld'
fileName = 'file0.jpg'
filePath = r'D:\桌面\mailFromAKing\file' + '\\'
mailFromLZY(subject, content, filePath, fileName, sendFile=True)
