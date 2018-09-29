REM 获取最新版本
PATH=%PATH%;C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\Common7\IDE\CommonExtensions\Microsoft\TeamFoundation\Team Explorer

tf get D:\_work\LMS\SRC-July-Aug /recursive /login:lms_tfs16,4567%%abc
PATH=%PATH%;C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\Common7\IDE

REM 编译发布
PATH=%PATH%;C:\Program Files (x86)\MSBuild\14.0\Bin
MSBuild.exe D:\_work\LMS\SRC-July-Aug\REL.Microsoft.KPSoft.Web\REL.Microsoft.KPSoft.Web.csproj /t:ResolveReferences;Compile /t:_CopyWebApplication /p:Configuration=Release /p:WebProjectOutputDir=D:\publish\LMSWeb /p:OutputPath=D:\publish\test

python 00321LMSAug142publish.py

pause