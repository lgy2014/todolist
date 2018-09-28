import os
import shutil
import stat
import re


def mycody(dir1, dir2, ignore=(".pdb")):
    if not os.path.exists(dir2):
        os.mkdir(dir2)
    list = os.listdir(dir1)
    for i in list:
        _src = os.path.join(dir1, i)
        if i.endswith(ignore):
            continue
        if os.path.isfile(_src):
            try:
                shutil.copy(_src, dir2)
                print(os.path.join(dir2, i))
            except PermissionError as err:
                print(err)
                # os.remove(os.path.join(dir2,i))
                os.chmod(os.path.join(dir2, i), stat.S_IWRITE)
                shutil.copy(_src, dir2)
                print(os.path.join(dir2, i))
        else:
            dstDir = os.path.join(dir2, i)
            srcDir = os.path.join(dir1, i)
            mycody(srcDir, dstDir, ignore=ignore)

# -------------------------------------


rootRegularList = []
regularList = []


def IgnoreToRegular(_str):
    _str=_str.replace('.','\\.')
    _str=_str.replace('*','.*')
    return _str.lower()


def ValidateRegular(regulars, item):
    for reg in regulars:
        if re.match(reg, item.lower()):
            return True
    return False

# 子目录拷贝


def _copydir(dir1, dir2,isRootDir=False):
    if not os.path.exists(dir2):
        os.mkdir(dir2)
    list = os.listdir(dir1)
    for i in list:
        _copyfile(dir1, dir2, i,isRootDir)


def _copyfile(dir1, dir2, i, isRootDir=False):
    _src = os.path.join(dir1, i)

    # 如果该项符合过滤条件则继续下一项
    if ValidateRegular(regularList, i):
        return
    if isRootDir and ValidateRegular(rootRegularList, i):
        return

    if os.path.isfile(_src):
        try:
            shutil.copy(_src, dir2)
            print(os.path.join(dir2, i))
        except PermissionError as err:
            print(err)
            os.chmod(os.path.join(dir2, i), stat.S_IWRITE)
            shutil.copy(_src, dir2)
            print(os.path.join(dir2, i))
    elif os.path.isdir(_src):
        dstDir = os.path.join(dir2, i)
        srcDir = os.path.join(dir1, i)
        _copydir(srcDir, dstDir)


def mycody2(dir1, dir2, ignore=[".pdb"]):
    # 首次处理过滤
    length = len(ignore)
    for i in range(length):
        if ignore[i].startswith('/'):
            item = ignore[i].lstrip('/')
            rootRegularList.append(IgnoreToRegular(item))
        else:
            regularList.append(IgnoreToRegular(ignore[i]))

    _copydir(dir1,dir2,True)
