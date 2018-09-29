REM 获取最新版本
PATH=%PATH%;C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\Common7\IDE\CommonExtensions\Microsoft\TeamFoundation\Team Explorer

tf get D:\_work\LMS\SRC-July-Aug /recursive /login:lms_tfs16,4567%%abc
PATH=%PATH%;C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\Common7\IDE

REM 编译发布
PATH=%PATH%;C:\Program Files (x86)\MSBuild\14.0\Bin
MSBuild.exe D:\_work\LMS\SRC-July-Aug\REL.Microsoft.KPSoft.Portal\REL.Microsoft.KPSoft.Web41.csproj /t:ResolveReferences;Compile /t:_CopyWebApplication /p:Configuration=Debug /p:WebProjectOutputDir=D:\LMS\Release41 /p:OutputPath=D:\publish\test

python 00341LMSAug142publish.py

pause