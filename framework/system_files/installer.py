import os,pip
import subprocess
import sys
from getAllFiles import getAllFIlesName

def install(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])

def installPip():
    print("downloading pip")
    # os.popen("curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py")
    # os.popen("get-pip.py")

def checkBothPackageList():
    help("modules")
    all_packages=list()
    reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
    installed_packages_list1 = [r.decode().split('==')[0] for r in reqs.split()]
    all_packages.extend(installed_packages_list1)
    installed_packages_list2 = list(sys.modules.keys())
    all_packages.extend(installed_packages_list2)
    return all_packages

def getLocalFiles(path):
    all_files = getAllFIlesName(path)
    local_files=list()
    for file_ in all_files:
        local_files.append(file_["file_name"].split(".")[0])
    return local_files

def IfInstalled(imported_files):
    installed_packages = checkBothPackageList()
    unInstalled_packages = list(filter(lambda imported_file: (imported_file not in installed_packages) , imported_files))
    return unInstalled_packages
        
