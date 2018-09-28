import os
import shutil
import util


# july 发布到 142 脚本
ignore_lms=(".pdb","TemplateFiles","AppOffLine","DownLoad","Test","UploadFile","EDI","TemplateFiles","Images","AppSettings.config","Blank.aspx","default.aspx","Error.aspx","FrameInfo.aspx","GetConfigurableId.ashx","Global.asax","HomePage.aspx","Index.aspx","log4net.config","packages.config","Web.config","注释.txt")

# ignore_lms = ignore_lms +("bin")
# ignore_lms = ignore_lms +("Styles")
# ignore_lms = ignore_lms +("Scripts")

src = u"D:\\a"
dst = u"D:\\b"
util.mycody(src,dst,ignore=ignore_lms)