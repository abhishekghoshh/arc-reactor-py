from system_files.utility.stringUtils import StringUtils
from functools import wraps

class ExceptionHandler:
    def __init__(self,*args, **kwargs):
        print(None)

    def __call__(self,func_):
        handleExceptionEnabled = "False"
        handleExceptionExitEnabled="False"
        if(StringUtils.stringEqualsIgnoreCase("Y",handleExceptionEnabled)):
            @wraps(func_)
            def wrapper(*args, **kwargs):
                try:
                    return_val = func_(*args, **kwargs)
                    return return_val
                except Exception as ex:
                    print(ex)
                    return ex
            return wrapper
        else:
            return func_