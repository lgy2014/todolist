import os
import shutil
import util

# july 发布到 142 脚本
ignore_lms=(".pdb","TemplateFiles","Styles","AppOffLine","DownLoad","Test","UploadFile","Images","EDIPAStyle","lib","jquery1.9.1","jquery-tmpl-master","kindeditor-3.4","layui","My97DatePicker","artdialog","SwfUpload","uploadify","ymPrompt","AppSettings.config","Blank.aspx","default.aspx","Error.aspx","FrameInfo.aspx","GetConfigurableId.ashx","Global.asax","HomePage.aspx","Index.aspx","log4net.config","packages.config","Web.config","注释.txt")

july1=u"D:\\publish\\LMSWeb"
july2=u"\\\\10.99.110.142\\d$\\LMS\\LMSJuly_21"
util.mycody(july1,july2,ignore=ignore_lms)