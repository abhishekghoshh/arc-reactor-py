import importlib
import inspect
from functools import wraps
from collections import namedtuple
from system_files.decorator.restrict import Restrict

@Restrict(frameworkOnly=True,access=["system_files","src"])
class Component:
    __singleton_container = dict()
    TYPE = namedtuple('_component', ['SINGLETON','PROTOTYPE','REQUEST'])("singleton","prototype","request")
    def __init__(self,*args, **kwargs):
        self.__value=kwargs.get('value',Component.TYPE.SINGLETON)
        
    def __call__(self,class_name):
        if(self.isClass(class_name)):
            if(self.__value == Component.TYPE.SINGLETON):
                return self.__buildSingletonComponent(class_name)
            elif(self.__value == Component.TYPE.PROTOTYPE):
                return self.__buildPrototypeComponent(class_name)
            elif(self.__value == Component.TYPE.REQUEST):
                return self.__buildRequestComponent(class_name)
            else:
                print("Your program is terminated forcefully")
                raise Exception('Error : ',self.__value ,'is not a proper type')
        else:
            print("remove @Component from",str(class_name).split(" ")[1])
            print("Your program is terminated forcefully")
            raise Exception('Error : Only class object can be component')
    
    def isClass(self,class_name):
        if("class" in str(class_name).split(" ")[0]):
            return True
        else:
            return False

    def __buildSingletonComponent(self,class_name):
        @wraps(class_name)
        def wrapper(*args, **kwargs):
            if(class_name.__name__ in Component.__singleton_container):
                return Component.__singleton_container[class_name.__name__]
            else:
                kwargs = initializeConstructor(*args, **kwargs)
                autowired_object = class_name(*args, **kwargs)
                Component.__singleton_container[class_name.__name__] = autowired_object 
                return autowired_object 
        def initializeConstructor(*args, **kwargs)-> dict:
            try:
                new_kwargs = kwargs.copy()
                for parameter in list(class_name.__init__.__code__.co_varnames):
                    autowired_class = inspect.signature(class_name.__init__).parameters[parameter].annotation
                    if(parameter=="self"):
                        continue
                    elif(str(autowired_class) == "<class 'inspect._empty'>"):
                        new_kwargs[parameter] = None
                    else:
                        new_kwargs[parameter] = autowired_class()
            except Exception as ex:
                print(ex)
            
            return new_kwargs
        return wrapper

    def __buildPrototypeComponent(self,class_name):
        @wraps(class_name)
        def wrapper(*args, **kwargs):
            return class_name(*args, **kwargs) 
        return wrapper

    def __buildRequestComponent(self,class_name):
        return class_name
    
    def class_obj(self,module_path,class_name):
        m = importlib.import_module(module_path)
        c = getattr(m, class_name)
        obj = c()
        return obj