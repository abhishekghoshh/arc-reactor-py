from system_files.utility.stringUtils import StringUtils

class PrettyError:
    def __init__(self,*args, **kwargs):
        print(None)

    def __call__(self,func_):
        handleExceptionEnabled = "Y"
        if(StringUtils.stringEqualsIgnoreCase("Y",handleExceptionEnabled)):
            @wraps(func_)
            def wrapper(*args, **kwargs):
                try:
                    return_val = func_(*args, **kwargs)
                    return return_val
                except Exception as ex:
                    print(ex)
                    exit(0)
            return wrapper
        else:
            return func_