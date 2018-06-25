import os
import shutil
import stat

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
                os.chmod(os.path.join(dir2,i), stat.S_IWRITE)
                shutil.copy(_src, dir2)
                print(os.path.join(dir2, i))
        else:
            dstDir = os.path.join(dir2, i)
            srcDir = os.path.join(dir1, i)
            mycody(srcDir, dstDir, ignore=ignore)