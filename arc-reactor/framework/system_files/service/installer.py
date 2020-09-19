import pip,os
from system_files.utility.commonUtils import CommonUtils
from system_files.utility.stringUtils import StringUtils
from system_files.decorator.component import Component

@Component()        
class InstallerService:
    def __init__(self):
        print("I am inside InstallerService __init__")
    
    def installPip(self):
        print("downloading pip feature is incomplete right now ")
        print("you can download it manually ")
        # os.popen("curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py")
        # os.popen("pip/get-pip.py")
        CommonUtils.askUserToStopExecution()
    
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
                CommonUtils.stopExecution()  
        else:
            CommonUtils.askUserToStopExecution()