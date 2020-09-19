from functools import wraps
from concurrent.futures import ThreadPoolExecutor
import importlib

class HystrixHandler:
    def __init__(self,*args, **kwargs):
        self.__fallbackMethod=kwargs.get('fallbackMethod',"fallback")
        self.__commandKey=kwargs.get('commandKey ',None)
        self.__ignoreExceptions=kwargs.get('ignoreExceptions',[])
        self.__thresoldTimeInMS=kwargs.get('thresoldTimeInMS',None)

    def __call__(self,func_):
        @wraps(func_)
        def wrapper(*args, **kwargs):
            try:
                [print(attr," : ",getattr(func_, attr)) for attr in type(func_).__dict__]
                # self.__module_name = func_.__code__
                # self.__class_name = func_.__qualname__.split(".")[0]
                # self.__called_method= func_.__qualname__.split(".")[1]
                # print(self.__class_name,self.__called_method)
                # # class_ = globals()[self.__class_name]()
                # # _f= func = getattr(class_, 'fallback')
                # # _f()
                # m = importlib.import_module("src.main.Class3")
                # c = getattr(m, "Class3")
                # obj = c()
                # obj.fallback()
                # method = getattr(obj, "myFallback")
                # method()
                return func_(*args, **kwargs)
            except Exception as ex:
                # try:
                #     m = globals()['A']()
                #     func = getattr(m, 'sampleFunc')
                #     method = getattr(my_cls, method_name)
                # except AttributeError:
                #     raise NotImplementedError("Class `{}` does not implement `{}`".format(my_cls.__class__.__name__, method_name))

                print(ex)
                return ex
        return wrapper

        def __register(self):
            pass
        def __traceFailure(self):
            pass
        def __anotherFailure(self):
            pass
        def __isDuplicateCommandKey(self):
            pass