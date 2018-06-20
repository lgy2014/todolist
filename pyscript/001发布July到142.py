import os
import shutil
import util

def mycodysimple(dir1,dir2):
    ignores=["AppOffLine","DownLoad","Test","UploadFile"]
    list=os.listdir(dir1)
    for i in list:
        if os.path.isdir(os.path.join(dir1,i)):
            if i in ignores:
                continue
            else:
                target=os.path.join(dir2,i)
                util.mycody(os.path.join(dir1,i),target)

# july 发布到 142 脚本
# july1=u"D:\\publish\\LMSWeb"
# july2=u"\\\\10.99.110.142\\d$\\LMS\\LMSJuly_21"

# copy(july1,july2)
