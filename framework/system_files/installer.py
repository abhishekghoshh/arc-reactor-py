import os,pip
import subprocess
import sys

def install(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])

def installPip():
    print("downloading pip")
    # os.popen("curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py")
    # os.popen("get-pip.py")

def IfInstalled(imported_files):
    reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
    installed_packages = [r.decode().split('==')[0] for r in reqs.split()]
    unInstalled_packages = list(filter(lambda imported_file: (imported_file not in installed_packages) , imported_files)) 
    return unInstalled_packages
        
