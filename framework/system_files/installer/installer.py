import subprocess,sys,pip,os
from system_files.utility.commonUtils import CommonUtils
from system_files.utility.stringUtils import StringUtils
from system_files.annotation.component import Component

@Component()
class Installer:
    def __int__(self,_util:CommonUtils,_stringUtil:StringUtils):
        self.util=_util
        self.stringUtil=_stringUtil

    def install(self,package):
        if(StringUtils.isStrNotBlank(package)):
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
                self.util.stopExecution()  
        else:
            self.util.askUserToStopExecution()

    def installPip(self):
        print("downloading pip feature is incomplete right now ")
        print("you can download it manually ")
        # os.popen("curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py")
        # os.popen("pip/get-pip.py")
        self.util.askUserToStopExecution()
        
