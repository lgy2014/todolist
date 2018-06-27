import os
import shutil
import util

# ignore_lms=("bin","Scripts","Styles","TemplateFiles","AppOffLine","DownLoad","Test","UploadFile","EDI","TemplateFiles","Images",".pdb","AppSettings.config","Blank.aspx","default.aspx","Error.aspx","FrameInfo.aspx","GetConfigurableId.ashx","Global.asax","HomePage.aspx","Index.aspx","log4net.config","packages.config","Web.config","注释.txt")
# july1=u"D:\\publish\\LMSWeb"
# julytest=u"D:\\publish\\test"
# util.mycody(july1,julytest,ignore=ignore_lms)



# july 发布到 142 脚本
ignore_lms=(".pdb","TemplateFiles","AppOffLine","DownLoad","Test","UploadFile","EDI","Images","jquery1.9.1","jquery-tmpl-master","kindeditor-3.4","layui","My97DatePicker","artdialog","SwfUpload","uploadify","ymPrompt","AppSettings.config","Blank.aspx","default.aspx","Error.aspx","FrameInfo.aspx","GetConfigurableId.ashx","Global.asax","HomePage.aspx","Index.aspx","log4net.config","packages.config","Web.config","注释.txt")

# ignore_lms = ignore_lms +("bin")
# ignore_lms = ignore_lms +("Styles")
# ignore_lms = ignore_lms +("Scripts")

july1=u"D:\\publish\\LMSWeb"
july2=u"\\\\10.99.110.142\\d$\\LMS\\LMSJuly_21"
util.mycody(july1,july2,ignore=ignore_lms)