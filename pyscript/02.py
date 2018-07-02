import re
import os


rootIgnore=[]
ignore=[]

ignore_lms=[".pdb","TemplateFiles","Styles","AppOffLine","DownLoad","Test","UploadFile","Images","EDIPAStyle","lib","jquery1.9.1","jquery-tmpl-master","kindeditor-3.4","layui","My97DatePicker","artdialog","SwfUpload","uploadify","ymPrompt","AppSettings.config","Blank.aspx","default.aspx","Error.aspx","FrameInfo.aspx","GetConfigurableId.ashx","Global.asax","HomePage.aspx","Index.aspx","log4net.config","/packages.config","/*.config","/*.txt"]

for i in ignore_lms:
    if i.startswith('/'):
        rootIgnore.append(i.lstrip('/'))
    else:
        ignore.append(i)

for i in range(len(rootIgnore)):
    if rootIgnore[i].startswith('*.'):
        rootIgnore[i]='.*\.'+rootIgnore[i]

for i in rootIgnore:
    print(i)


def mymatch(str):
    for patter in rootIgnore:
        if re.match(patter,str):
            return True
        else:
            return False


    
