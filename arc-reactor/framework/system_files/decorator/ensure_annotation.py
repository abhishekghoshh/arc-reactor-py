from system_files.utility.stringUtils import StringUtils
from functools import wraps

 

class EnsureAnnotation:
    def __init__(self,*args, **kwargs):
        pass

    def __call__(self,func_):
        ensureAnnotationEnabled = "Y"
        if(StringUtils.stringEqualsIgnoreCase("Y",ensureAnnotationEnabled)):
            from functools import wraps
            from inspect import getcallargs
            @wraps(f)
            def wrapper(*args, **kwargs):
                for arg, val in getcallargs(func_, *args, **kwargs).items():
                    print(arg,val)
                    if arg in func_.__annotations__:
                        templ = func_.__annotations__[arg]
                        print(templ)
                        # msg = "Argument {arg} to {f} does not match annotation type {t}"
                        # Check(val).is_a(templ).or_raise(EnsureError, msg.format(arg=arg, f=f, t=templ))
                return_val = func_(*args, **kwargs)
                if 'return' in func_.__annotations__:
                    templ = func_.__annotations__['return']
                    msg = "Return value of {f} does not match annotation type {t}"
                    # Check(return_val).is_a(templ).or_raise(EnsureError, msg.format(f=f, t=templ))
                return return_val
            return wrapper
        else:
            return func_