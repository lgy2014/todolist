import util

# 过滤掉常规文件，加快发布速度
ignore=['/AppOffLine','/*.config','/*.aspx','/*.ashx','/*.asax','/*.txt','/Styles','/DownLoad','/Test','*.zip','*.rar','*.pdb','temp*','images','bootstrap*','jquery*','artdialog*','echarts*','kindeditor*','layui','my97datepic*','swfupload*','ymprompt*','uploadfile*','npoi*','lenovo*.dll','microsoft*','QuotationModel','ContractModel']

# full
# ignore=['*.pdb','/test','/AppOffLine','/*.config','/*.aspx','/*.ashx','/*.asax','/*.txt']

path="D:\\LMS\\Release41"
path2="\\\\10.99.110.142\\d$\\LMSATS41"


util.mycody2(path,path2,ignore)