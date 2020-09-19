from system_files.utility.stringUtils import StringUtils
import sys,os
import warnings
import ast
import types


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
    

    
    


