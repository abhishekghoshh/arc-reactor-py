from arc_reactor.utility.stringUtils import StringUtils
from arc_reactor.utility.commonUtils import CommonUtils
from functools import wraps


class DisablePrint:
    def __init__(self,*args, **kwargs):
        pass

    def __call__(self,func_):
        printNothingEnabled = "Y"
        if(StringUtils.stringEqualsIgnoreCase("Y",printNothingEnabled)):
            @wraps(func_)
            def wrapper(*args, **kwargs):
                CommonUtils.blockPrint()
                return_val = func_(*args, **kwargs)
                CommonUtils.enablePrint()
                return return_val
            return wrapper
        else:
            return func_