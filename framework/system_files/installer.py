import os,pip
def install(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])

def installPip():
    print("downloading pip")
    # os.popen("curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py")
    # os.popen("get-pip.py")

def IfInstalled():
    return False

        
