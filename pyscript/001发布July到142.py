import os
import shutil
import util


def mycodysimple(dir1,dir2):
    ignores=["AppOffLine","DownLoad","Test","UploadFile","EDI","TemplateFiles","Images"]
    list=os.listdir(dir1)
    for i in list:
        if os.path.isdir(os.path.join(dir1,i)):
            if i in ignores:
                continue
            else:
                target=os.path.join(dir2,i)
                util.mycody(os.path.join(dir1,i),target)

# july 发布到 142 脚本
july1=u"D:\\publish\\LMSWeb"
july2=u"\\\\10.99.110.142\\d$\\LMS\\LMSJuly_21"

# mycodysimple(july1,july2)

# ignore_lms=("AppOffLine","DownLoad","Test","UploadFile","EDI","TemplateFiles","Images",".pdb","AppSettings.config","Blank.aspx","default.aspx","Error.aspx","FrameInfo.aspx","GetConfigurableId.ashx","Global.asax","HomePage.aspx","Index.aspx","log4net.config","packages.config","Web.config","注释.txt")
ignore_lms=("bin","Scripts","Styles","TemplateFiles","AppOffLine","DownLoad","Test","UploadFile","EDI","TemplateFiles","Images",".pdb","AppSettings.config","Blank.aspx","default.aspx","Error.aspx","FrameInfo.aspx","GetConfigurableId.ashx","Global.asax","HomePage.aspx","Index.aspx","log4net.config","packages.config","Web.config","注释.txt")


julytest=u"D:\\publish\\test"
util.mycody(july1,julytest,ignore=ignore_lms)