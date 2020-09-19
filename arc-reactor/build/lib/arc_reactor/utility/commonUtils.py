from arc_reactor.utility.stringUtils import StringUtils
import sys,os
import warnings
import ast
import types
import sys,urllib


class CommonUtils:
    def __init__(self):
        print(None)

    @staticmethod
    def getRealValue(val_):
        return ast.literal_eval(val_)

    @staticmethod
    def isMethod(method_name):
        return isinstance(method_name, types.MethodType)

    @staticmethod
    def isFunction(fun_name):
        return isinstance(fun_name, types.FunctionType)
    
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
        if(StringUtils.stringEqualsIgnoreCase("Y",warningEnabled)):
            CommonUtils.stopWarning()

    @staticmethod
    def stopWarning():
        warnings.filterwarnings("ignore")

    @staticmethod
    def blockPrint():
        sys.stdout = open(os.devnull, 'w')

    @staticmethod
    def enablePrint():
        sys.stdout = sys.__stdout__

    @staticmethod
    def checkInternetAvailable():
        try :
            data = urllib.urlopen("https://www.google.co.in")
            return True
        except Exception as ex:
            return False

    @staticmethod
    def pythonVersion():
        if sys.version_info.major < 3:
            print('Upgrade to Python 3')
            askUserToStopExecution()
        else:
            print("Your python version is ",sys.version)

    
    


