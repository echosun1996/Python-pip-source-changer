#!/usr/bin/env python
#coding=utf-8
import platform
import os

def mkdir(path):
    path=path.strip().rstrip("\\")
    isExists=os.path.exists(path)
    if not isExists:
        os.makedirs(path) 
        print(path+' Create finish/')
        return True
    else:
        print(path+' Directory already exists.')
        return False

def mkfile(filepath):
    pipfile = "[global]\ntrusted-host=mirrors.aliyun.com\nindex-url=http://mirrors.aliyun.com/pypi/simple/"
    if os.path.exists(filepath):
        if str(input("File exist!Cover?(Y/N))")).upper() == 'N':
            print("Not Cover.")
            return
    with open(filepath, 'w') as fp:
        fp.write(pipfile)
    print("Wirte finish.")

def platformSelect( ):
    sysstr = platform.system()
    if(sysstr =="Windows"):
        print("System type: Windows")
        path=os.getenv('HOMEPATH')+"\\pip"
        mkdir(path)
        mkfile(path+'\\pip.ini')
        
    elif(sysstr == "Linux"):
        print("System type: Linux")
        path="~/.pip/"
        mkdir(path)
        mkfile(path+'\\pip.conf')
    else:
        print ("Other System tasks")

if __name__ == "__main__" :
    platformSelect()
