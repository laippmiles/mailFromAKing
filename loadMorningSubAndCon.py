def loadMorningSubAndCon():
    from random import uniform
    SSRlist = ['我对你好，不需要原因。',
                '没关系，我有耐心，等你慢慢开窍。',
                '我从未如此想要靠近一个人。',
                '想让我后悔的话，就不要在这种地方倒下。',
                '即使末日来临，我也会陪在你身边。'
                ]
    SRlist = ['在眼中，万般风景不如你。',
              '我世界中唯一的变数就是你。',
              '不知为什么，面对你，我总能卸下心防。',
              '或许我已经等不及让你慢慢开窍了。',
              '我正好在外面，咳，带你出去吃早餐。'
              ]
    Rlist = ['每个人都有很多面，不像你只有儍的一面。',
             '你的身体，你不关心，可是我关心。',
             '这就是你给我的礼物？好吧，我勉强收下。',
             '不仅要占领你的心，还要占领你的胃。',
             '专心创作吧，应酬和交际，交给我就好。',
             '我有哪次没有出手帮你。',
             '以后遇到问题，该找我就不要傻扛着。',
            ]
    morningList = ['记得吃早饭。',
                   '早安，笨蛋。',
                   '早上好，别再赖床了',
                ]
    ballot = int(uniform(0,101))
    if ballot >= 0 and ballot <= 20 :
        SSRindex = int(uniform(0,len(SSRlist)))
        subject = SSRlist[SSRindex]
    elif ballot >=21 and ballot <= 50:
        SRindex = int(uniform(0,len(SRlist)))
        subject = SRlist[SRindex]
    else:
        Rindex = int(uniform(0,len(Rlist)))
        subject = Rlist[Rindex]

    contentIndex = int(uniform(0,len(morningList)))
    content = morningList[contentIndex]

    return subject, content
