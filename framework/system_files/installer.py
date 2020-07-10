import subprocess,sys,pip,os
from system_files.utility import blockPrint,enablePrint,isStrNotBlank,askUserToStopExecution,stopExecution

def install(package):
    if(isStrNotBlank(package)):
        try:
            print(package +" is installing")
            if hasattr(pip, 'main'):
                pip.main(['install', package])
            else:
                pip._internal.main(['install', package])
            print(package +" downloading complete")
        except Exception as ex:
            print(ex)
            print("Stopping python program")
            print(package+" package is not downloaded")
            stopExecution()  
    else:
        askUserToStopExecution()

def installPip():
    print("downloading pip feature is incomplete right now ")
    print("you can download it manually ")
    # os.popen("curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py")
    # os.popen("pip/get-pip.py")
    askUserToStopExecution()
        
