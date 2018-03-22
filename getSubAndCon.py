from random import uniform
from loadNormalSubAndCon import loadNormalSubAndCon
from loadMorningSubAndCon import loadMorningSubAndCon
from loadAfternoonSubAndCon import loadAfternoonSubAndCon
from loadNightSubAndCon import loadNightSubAndCon
def getSubAndCon(mailTime,h):
    subject = '如果你看到了这个标题'
    content = '请去联系那条蠢狗'
    if mailTime == h[0]:#第一个时段
        subject, content = loadMorningSubAndCon()
        return subject,content
    elif mailTime == h[1]:#第二个时段
        subject, content = loadAfternoonSubAndCon()
        return subject, content
    elif mailTime == h[2]:#第三个时段
        subject, content = loadNightSubAndCon()
        return subject, content
    else:
        return subject, content

h = [8,14,23]
hour = 23
print(getSubAndCon(hour,h))