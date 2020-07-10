import sys,os
import warnings

def stopWarningWithConfigValue():
    warningEnabled = "Y"
    if(stringEqualsIgnoreCase("N",warningEnabled)):
        stopWarning()

def stopWarning():
    warnings.filterwarnings("ignore")

# Disable
def blockPrint():
    sys.stdout = open(os.devnull, 'w')
# Restore
def enablePrint():
    sys.stdout = sys.__stdout__

def isStrNotBlank(name_):
    return bool(name_ and name_.strip())

def isString(str_):
    return None!= str_ and type(str_) == str

def stringEqualsIgnoreCase(str1,str2):
    if isString(str1) and isString(str2):
        return str1.lower() == str2.lower()

def stopExecution():
    exit(1)

def askUserToStopExecution():
    user_input=str(input("stop excecution [Y/N] : "))
    if stringEqualsIgnoreCase("Y",user_input):
        stopExecution()
    else:
        pass


