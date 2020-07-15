from system_files.utility.stringUtils import StringUtils
import sys,os
import warnings


class CommonUtils:
    def __init__(self):
        print(None)

    @staticmethod
    def stopExecution():
        exit(1)

    @staticmethod
    def askUserToStopExecution():
        user_input=str(input("stop excecution [Y/N] : "))
        if StringUtils.stringEqualsIgnoreCase("Y",user_input):
            CommonUtils.stopExecution()
        else:
            pass

    @staticmethod
    def stopWarningWithConfigValue():
        warningEnabled = "Y"
        if(StringUtils.stringEqualsIgnoreCase("N",warningEnabled)):
            stopWarning()

    @staticmethod
    def stopWarning():
        warnings.filterwarnings("ignore")

    @staticmethod
    def blockPrint():
        sys.stdout = open(os.devnull, 'w')

    @staticmethod
    def enablePrint():
        sys.stdout = sys.__stdout__


