import util

# 过滤掉常规文件，加快发布速度
ignore=['/AppOffLine','/*.config','/*.aspx','/*.ashx','/*.asax','/*.txt','/Styles','/DownLoad','/Test','*.zip','*.rar','*.pdb','temp*','images','bootstrap*','jquery*','artdialog*','echarts*','kindeditor*','layui','my97datepic*','swfupload*','ymprompt*','uploadfile*','npoi*','lenovo*.dll','DC.Web.HttpCompress.dll','DropDownCheckList.dll','BouncyCastle.Crypto.dll','ComponentArt.Web.UI.dll','EntityFramewor*.dll','ICSharpCode.SharpZipLib.dll','Ionic.Zip.dll','ItrusDotNetCertAPI 1.2.dll','log4net.DLL','Newtonsoft.Json.dll','Syste*.dll','SAP.Conne*.dll','microsoft*','QuotationModel','ContractModel','/plugins','/themes']

# full
# ignore=['*.pdb','/test','/AppOffLine','/*.config','/*.aspx','/*.ashx','/*.asax','/*.txt']

path="D:\\publish\\LMSWeb"
path2="\\\\10.99.110.142\\d$\\LMSATS21"

# path2="D:\\publish\\test"

util.mycody2(path,path2,ignore)