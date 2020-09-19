import git,os,shutil
import stat
from pyzip import PyZip
from pyfolder import PyFolder
from arc_reactor.constant.frameworkZip import frameworkZipData
import os

def iniatiateFramework():
    zipUnZipFrameWork()
    # installProjectFromGit()

def zipUnZipFrameWork():
    try:
        directory = (os.getcwd())
        changePermission(directory)
        removeTree(directory)
        pyzip = PyZip().from_bytes(frameworkZipData)
        pyzip.save("code.zip")
        zip_path = os.path.join(directory,"code.zip")
        pyzip = PyZip(PyFolder(directory, interpret=False)).from_file(zip_path, inflate=False)
        os.remove("code.zip")
    except Exception as ex:
        print(ex)

def removeTree(directory):
    try:
        if(len(os.listdir(directory))!=0):
            userInput= str(input("Do you want to clean your repository [Y/N]: "))
            if(userInput == "Y" or userInput == "y"):
                shutil.rmtree(directory)
    except Exception as ex:
        # print("inside removeTree")
        # print(ex)
        pass

def changePermission(path,permission=stat.S_IWUSR):
    try:
        root_dir=os.listdir(path)
        if(len(root_dir)!=0):
            for content in root_dir:
                current_path= os.path.join(path,content)
                if os.path.isdir(path+"\\"+content):
                    changePermission(path+"\\"+content,permission)
                if os.path.isfile(path+"\\"+content):
                    os.chmod(current_path,stat.S_IWUSR)
    except Exception as e:
        print("inside changePermission")
        print(e)

def installProjectFromGit():
    try:
        directory = (os.getcwd())
        changePermission(directory)
        removeTree(directory)
        url = "https://github.com/Abhishek1009/python-projects.git"
        git.Git(directory).clone(url)
        removeOthers(directory) 
    except Exception as ex:
        print(ex)

def removeOthers(directory):
    path = r"python-projects\arc-reactor\framework.v2"
    removeFolderPath = os.path.join(directory,r"python-projects")
    actualPath=os.path.join(directory,path)
    for content in os.listdir(actualPath):
        contentPath = os.path.join(actualPath,content)
        shutil.move(contentPath, directory)
    changePermission(removeFolderPath)
    removeTree(removeFolderPath)
