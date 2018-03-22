def loadAfternoonSubAndCon():
    from random import uniform
    subject = '如果你看到了这个标题'
    content = '请去联系那条蠢狗'

    SSRlist = ['我对你好，不需要原因。',
               '没关系，我有耐心，等你慢慢开窍。',
               '我从未如此想要靠近一个人。',
               '想让我后悔的话，就不要在这种地方倒下。',
               '即使末日来临，我也会陪在你身边。'
               ]
    SRlist = ['不要再自作聪明，撮合我和其他人了。',
              '我也很幵心，因为你这么开心。',
              '你究竟什么时候才能明白呢？',
              '打算就这么走了吗？跟我共舞一曲如何。'
              ]
    Rlist = ['你是我亲自培养的，怎能允许他人否定。',
             '懒惰只能造成失败，打起精神来吧！',
             '我会赔偿你，被我毀掉的一半假期。',
             '这是我给你下达的命令，不许不遵从。',
             '录完节目后，完整出现在我面前。',
             '你不必羡慕，只要努力，你也会有。',
             '刚才说话太严厉了吗？抱歉。',
             '下次不准再不接我电话。'
            ]
    afternoonList = ['下午好。',
                   '午安，笨蛋。',
                   '午安。',
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

    contentIndex = int(uniform(0,len(afternoonList)))
    content = afternoonList[contentIndex]

    return subject, content