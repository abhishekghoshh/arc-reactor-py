from system_files.utility.stringUtils import StringUtils
from functools import wraps


class EntryExitMethodLogger:
    def __init__(self,*args, **kwargs):
        pass

    def __call__(self,func_):
        entryExitMethodLoggerEnabled = "Y"
        if(StringUtils.stringEqualsIgnoreCase("Y",entryExitMethodLoggerEnabled)):
            @wraps(func_)
            def wrapper(*args, **kwargs):
                #add logger for entry
                print("Entering",func_.__name__+"()")
                return_val = func_(*args, **kwargs)
                #add logger for exit
                print("exiting",func_.__name__+"()")
                return return_val
            return wrapper
        else:
            return func_