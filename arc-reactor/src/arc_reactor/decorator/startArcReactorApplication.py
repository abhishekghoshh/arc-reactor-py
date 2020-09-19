from arc_reactor.service.sysService import SysService


class StartArcReactorApplication:
    def __init__(self,*args, **kwargs):  
        self.__setup()
        
    def __call__(self,func_):
        return func_

    def __setup(self):
        self.__sysServiceSetUp()

    def __sysServiceSetUp(self):
        self.__sysService= SysService() 
        self.__sysService.stopWarning()
        self.__sysService.pythonVersion()
        self.__sysService.setConfigReader()