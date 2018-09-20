def FormatTime(second):
    desc=''

    hour = second // 3600
    second= second % 3600

    minute = second // 60
    second = second % 60

    if  second>0:
        desc ='%d 秒'%(second)
    if  minute >0:
        desc='%d 分钟 '%(minute)+desc
    if  hour>0:
        desc= '%d 小时 '%(hour)+desc

    return desc

ss = FormatTime(29)
print (ss)

ss = FormatTime(1029)
print (ss)

ss = FormatTime(15059)
print (ss)