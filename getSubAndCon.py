from random import uniform
from loadNormalSubAndCon import loadNormalSubAndCon
from loadMorningSubAndCon import loadMorningSubAndCon
from loadAfternoonSubAndCon import loadAfternoonSubAndCon
from loadNightSubAndCon import loadNightSubAndCon
def getSubAndCon(mailTime):

    if mailTime == 8:
        morningList, morningKeyList = loadMorningSubAndCon()
        index = int(uniform(0,len(morningKeyList)))
        subject = morningKeyList[index]
        content = morningList[subject]
        return subject,content
    elif mailTime == 14:
        afternoonList, afternoonKeyList = loadAfternoonSubAndCon()
        index = int(uniform(0, len(afternoonList)))
        subject = afternoonKeyList[index]
        content = afternoonList[subject]
        return subject, content
    elif mailTime == 20:
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