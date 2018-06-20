import os
import shutil
import util

def mycodysimple(dir1,dir2):
    ignores=["css"]
    list=os.listdir(dir1)
    for i in list:
        if os.path.isdir(os.path.join(dir1,i)):
            if i in ignores:
                continue
            else:
                target=os.path.join(dir2,i)
                util.mycody(os.path.join(dir1,i),target)

src = u"D:\\a"
dst = u"D:\\b"
mycodysimple(src,dst)
