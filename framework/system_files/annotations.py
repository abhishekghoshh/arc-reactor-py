from system_files.utility import stringEqualsIgnoreCase,blockPrint,enablePrint
from functools import wraps
from inspect import getcallargs

def printNothing(func_):
    # print("value is ",value)
    printNothingEnabled = "Y"
    if(stringEqualsIgnoreCase("Y",printNothingEnabled)):
        @wraps(func_)
        def wrapper(*args, **kwargs):
            # for arg, val in getcallargs(f, *args, **kwargs).items():
            #     print(arg, val)
            blockPrint()
            return_val = func_(*args, **kwargs)
            enablePrint()
            return return_val
        return wrapper
    else:
        return func_
    
def logger(func_):
    loggerEnabled = "Y"
    if(stringEqualsIgnoreCase("Y",loggerEnabled)):
        @wraps(func_)
        def wrapper(*args, **kwargs):
            print("Entering",func_.__name__+"()")
            return_val = func_(*args, **kwargs)
            print("exiting",func_.__name__+"()")
            return return_val
        return wrapper
    else:
        return func_

def ensure_annotations(f):
    from functools import wraps
    from inspect import getcallargs
    @wraps(f)
    def wrapper(*args, **kwargs):
        for arg, val in getcallargs(f, *args, **kwargs).items():
            if arg in f.__annotations__:
                templ = f.__annotations__[arg]
                msg = "Argument {arg} to {f} does not match annotation type {t}"
                # Check(val).is_a(templ).or_raise(EnsureError, msg.format(arg=arg, f=f, t=templ))
        return_val = f(*args, **kwargs)
        if 'return' in f.__annotations__:
            templ = f.__annotations__['return']
            msg = "Return value of {f} does not match annotation type {t}"
            # Check(return_val).is_a(templ).or_raise(EnsureError, msg.format(f=f, t=templ))
        return return_val
    return wrapper