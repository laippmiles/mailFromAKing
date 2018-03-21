from random import uniform
from loadNormalSubAndCon import loadNormalSubAndCon
from loadMorningSubAndCon import loadMorningSubAndCon
from loadAfternoonSubAndCon import loadAfternoonSubAndCon
from loadNightSubAndCon import loadNightSubAndCon
def getSubAndCon(mailTime,h):

    if mailTime == h[0]:#第一个时段
        morningList, morningKeyList = loadMorningSubAndCon()
        index = int(uniform(0,len(morningKeyList)))
        subject = morningKeyList[index]
        content = morningList[subject]
        return subject,content
    elif mailTime == h[1]:#第二个时段
        afternoonList, afternoonKeyList = loadAfternoonSubAndCon()
        index = int(uniform(0, len(afternoonList)))
        subject = afternoonKeyList[index]
        content = afternoonList[subject]
        return subject, content
    elif mailTime == h[2]:#第三个时段
        nightList, nightKeyList = loadNightSubAndCon()
        index = int(uniform(0, len(nightList)))
        subject = nightKeyList[index]
        content = nightList[subject]
        return subject, content
    else:
        normalList, normalKeyList = loadNormalSubAndCon()
        index = int(uniform(0, len(normalKeyList)))
        subject = normalKeyList[index]
        content = normalList[subject]
        return subject, content
#print(getSubAndCon())