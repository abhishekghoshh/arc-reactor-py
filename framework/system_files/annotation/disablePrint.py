from system_files.utility.stringUtils import stringUtils


class DisablePrint:
    def __init__(self,*args, **kwargs):
        print(None)

    def __call__(self,func_):
        printNothingEnabled = "Y"
        if(stringEqualsIgnoreCase("Y",printNothingEnabled)):
            @wraps(func_)
            def wrapper(*args, **kwargs):
                self.blockPrint()
                return_val = func_(*args, **kwargs)
                self.enablePrint()
                return return_val
            return wrapper
        else:
            return func_