def loadNightSubAndCon():
    nightList = {
        '还在工作？': '今晚不要熬夜了。',
        '还在跑实验？': '不要只顾着等实验结果，多看些文献吧。',
        '还在写代码？': '晚上不要再喝咖啡了，会失眠。',
    }
    nightKeyList = list(nightList.keys())
    return nightList, nightKeyList