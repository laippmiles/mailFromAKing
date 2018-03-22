def loadNightSubAndCon():
    from random import uniform
    subject = '如果你看到了这个标题'
    content = '请去联系那条蠢狗'

    SSRlist = ['我对你好，不需要原因。',
                '没关系，我有耐心，等你慢慢开窍。',
                '我从未如此想要靠近一个人。',
                '想让我后悔的话，就不要在这种地方倒下。',
                '即使末日来临，我也会陪在你身边。'
                ]
    SRlist = ['帮别人完成工作，熬到深夜， 你傻吗？',
              '我想......一直和你在一起。',
              '雨要到后半夜才停，坐我的车回去吧。',
              '我疲惫的一面只在你面前展现。',
              '晤......谢谢你能理解我。',
             ]
    Rlist = ['时间静止只为与你相遇。',
             '汽水容易失眠，喝一杯牛奶吧。',
             '如果睡不着，允许你找我闲聊。',
             '对我来说，能看到你的笑容就好。',
             '无论什么要求，我都会满足你。',
             '在我面前，还是实话实说比较好。',
             '我可以给你带各地的纪念品。',
             '我没有意见，这次你做得很好。',
            ]
    nightList = ['少吃点夜宵。',
                   '晚安，笨蛋。',
                   '晚上好，不要熬夜了',
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

    contentIndex = int(uniform(0,len(nightList)))
    content = nightList[contentIndex]

    return subject, content