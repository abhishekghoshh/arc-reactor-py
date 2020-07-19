from functools import wraps
from system_files.decorator.restrict import Restrict

class Restriction:
    def __init__(self,*args, **kwargs):
       pass

    def __call__(self,func_):
        @Restrict(frameworkOnly=False,access=["system_files","src\main"])
        @wraps(func_)
        def wrapper(*args, **kwargs):
            print("hi")
            return func_(*args, **kwargs)
        return wrapper