from system_files.utility.configReader import ConfigReader
from system_files.utility.commonUtils import CommonUtils
from system_files.service.sysService import SysService
import os

class StartPythonApplication:
    def __init__(self,*args, **kwargs):
        print("StartPythonApplication __init__")
        self.__sysService= SysService()    
        self.__setup()
        

    def __call__(self,func_):
        return func_

    def __setup(self):
        self.__setConfigReader()
        CommonUtils.stopWarningWithConfigValue()
        self.__sysService.isPipAvailable()
        self.__sysService.pythonVersion()
        self.__checkDependency("system_files","src")

    def __checkDependency(self,*args):
        if(len(args)>0):
            for arg in args:
                try:
                    self.__sysService.dependencySetup(os.path.join(os.getcwd(),arg))
                except Exception as ex:
                    print(ex)
    
    def __setConfigReader(self):
        cr = ConfigReader()
        cr.setConfigForPath(os.path.join(os.getcwd(),r"system_files\system_config"))
        cr.setConfigForPath(os.path.join(os.getcwd(),r"src\configs"))