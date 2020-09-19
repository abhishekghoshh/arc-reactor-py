import inspect
import os
import types
from functools import wraps
from collections import namedtuple

class Restrict:
    __FRAMEWORK_ENTRY_POINT=namedtuple('_component', ['PATH'])(r"system_files\decorator\startPythonApplication.py")
    __satck_removal_list=['<frozen importlib._bootstrap>','<frozen importlib._bootstrap_external>']
    def __init__(self,*args, **kwargs):
        self.__callViaFrameWorkOnlyFlag = kwargs.get("frameworkOnly",False)
        self.__validPath = kwargs.get("access",["system_files"])
        
    def __call__(self,func_):
        @wraps(func_)
        def wrapper(*args, **kwargs):
            print(str(func_),"----------------------------")
            __frame_stack=inspect.stack()
            self.__addToStack(__frame_stack)
            [print(filename)for filename in self.__stack]
            # print(func_,"----------------------------")
            self.__callViaFrameWorkOnly(func_)
            if(self.__callViaAccesiblePathOnly(func_)):
                print("Valid directory file is accessing")
            else:
                print("you must give access to the directory, It will throw error in future")
            return func_(*args, **kwargs)
        return wrapper

    def __callViaFrameWorkOnly(self,func_):
        __absolute_path=os.path.join(os.getcwd(),Restrict.__FRAMEWORK_ENTRY_POINT.PATH)
        if(type(self.__callViaFrameWorkOnlyFlag) ==  type(True)):
            if(self.__callViaFrameWorkOnlyFlag and not self.__stack[-2]==__absolute_path):
                print(str(func_).split(" ")[1].strip("<"),"is a framework only class, It will throw error in future")
        else:
            print("frameworkOnly must be a boolean")
            raise Exception("frameworkOnly must be a boolean")
    
    def __callViaAccesiblePathOnly(self,func_):
        if(isinstance(self.__validPath, list)):
            for __path in self.__validPath:
                __actual_path = os.path.join(os.getcwd(),__path)
                if(not os.path.isdir(__actual_path)):
                    raise Exception(__actual_path,"is not a valid path")
                __actual_path_length = len(__actual_path)
                if(__actual_path == self.__stack[1][0:__actual_path_length]):
                    return True
                # print(__actual_path)
                # print(self.__stack[1][0:__actual_path_length])
            return False
            
        else:
            raise Exception("access must be list of valid path/paths")

    def __addToStack(self,stackTraceList):
        __stack=list()
        __current_frame_filename=stackTraceList[0].filename
        __stack.append(__current_frame_filename)
        for frame in stackTraceList:
            if(frame.filename != __current_frame_filename and frame.filename not in Restrict.__satck_removal_list):
                __current_frame_filename=frame.filename
                __stack.append(__current_frame_filename)
        self.__stack =  __stack
