import util
import time

start_time = time.time()
# 过滤掉常规文件，加快发布速度
ignore = ['/AppOffLine', '/*.config', '/*.aspx', '/*.ashx', '/*.asax', '/*.txt', '/Styles', '/DownLoad', '/Test', '*.zip', '*.rar', '*.pdb', 'temp*', 'images', 'bootstrap*', 'jquery*', 'artdialog*', 'echarts*', 'kindeditor*', 'layui', 'my97datepic*', 'swfupload*', 'ymprompt*', 'uploadfile*', 'npoi*', 'lenovo*.dll', 'DC.Web.HttpCompress.dll',
          'DropDownCheckList.dll', 'BouncyCastle.Crypto.dll', 'ComponentArt.Web.UI.dll', 'EntityFramewor*.dll', 'ICSharpCode.SharpZipLib.dll', 'Ionic.Zip.dll', 'ItrusDotNetCertAPI 1.2.dll', 'log4net.DLL', 'Newtonsoft.Json.dll', 'Syste*.dll', 'SAP.Conne*.dll', 'microsoft*', 'QuotationModel', 'ContractModel', '/plugins', '/themes']

# full
# ignore=['*.pdb','/test','/AppOffLine','/*.config','/*.aspx','/*.ashx','/*.asax','/*.txt']

path="D:\\LMS\\Release41"
path2="\\\\10.99.110.142\\d$\\LMSATS41"


util.mycody2(path, path2, ignore)

end_time = time.time()

timelen = end_time-start_time
timelen = FormatTime(timelen)
print('执行时长：', timelen)