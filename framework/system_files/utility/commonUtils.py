from system_files.annotation.component import Component
from system_files.utility.stringUtils import StringUtils
import sys,os
import warnings

@Component()
class CommonUtils:
    def __init__(self,_stringUtils:StringUtils):
        self.stringUtils = _stringUtils

    def stopExecution(self):
        exit(1)

    def askUserToStopExecution(self):
        user_input=str(input("stop excecution [Y/N] : "))
        if StringUtils.stringEqualsIgnoreCase("Y",user_input):
            self.stopExecution()
        else:
            pass
    
    def stopWarningWithConfigValue(self):
        warningEnabled = "Y"
        if(StringUtils.stringEqualsIgnoreCase("N",warningEnabled)):
            stopWarning()

    def stopWarning(self):
        warnings.filterwarnings("ignore")

    # Disable
    def blockPrint(self):
        sys.stdout = open(os.devnull, 'w')
    # Restore
    def enablePrint(self):
        sys.stdout = sys.__stdout__


