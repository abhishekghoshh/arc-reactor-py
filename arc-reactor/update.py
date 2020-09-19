from pyzip import PyZip
from pyfolder import PyFolder
import os


def update():
    updateFrameworkZipData(r"framework.v2",r"src\arc_reactor\constant\frameworkZip.py")
    updateArcReactorPathList(r"src\arc_reactor",r"src\arc_reactor\constant\packageFilesList.py")

def updateArcReactorPathList(packagePath,destinationPath):
    packageFilesList=list()
    updateAllPackagepath(os.path.join(os.getcwd(),packagePath),packageFilesList)
    savePackageFilesList(destinationPath,packageFilesList)

def savePackageFilesList(destinationPath,packageFilesList):
    try:
        destinationPath=os.path.join(os.getcwd(),destinationPath)
        f = open(destinationPath, "w")
        f.write("packageFilesListData="+str(packageFilesList))
        f.close()
    except Exception as ex:
        print(ex)
        raise ex
    

def updateFrameworkZipData(relativeFrameworkPath,zipDumpPath):
    try:
        frameworkPath = os.path.join(os.getcwd(),relativeFrameworkPath)
        pyzip = PyZip(PyFolder(frameworkPath, interpret=False))
        destinationPath = os.path.join(os.getcwd(),zipDumpPath)
        f = open(destinationPath, "w")
        f.write("frameworkZipData="+str(pyzip.to_bytes()))
        f.close()
    except Exception as ex:
        print(ex)
        raise ex


def updateAllPackagepath(path,packageFilesList):
    try:
        root_dir=os.listdir(path)
        if(len(root_dir)!=0):
            for content in root_dir:
                if("__pycache__" not in content):
                    current_path= os.path.join(path,content)
                    if os.path.isdir(current_path):
                        updateAllPackagepath(current_path,packageFilesList)
                    if os.path.isfile(current_path):
                        startIdx = current_path.find("arc_reactor")
                        packageFilesList.append(current_path[startIdx:])
    except Exception as e:
        print(e)

def clean(path):
    pass