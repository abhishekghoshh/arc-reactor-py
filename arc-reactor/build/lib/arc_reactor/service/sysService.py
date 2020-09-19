from arc_reactor.decorator.component import Component
from arc_reactor.utility.configReader import ConfigReader
from arc_reactor.utility.commonUtils import CommonUtils
from arc_reactor.decorator.restrict import Restrict

@Restrict(frameworkOnly=True,access=["system_files"])
@Component()
class SysService:
    def __init__(self):
        pass

    def pythonVersion(self):
        CommonUtils.pythonVersion()

    def setConfigReader(self):
        cr = ConfigReader()
    
    def stopWarning(self):
        CommonUtils.stopWarningWithConfigValue()