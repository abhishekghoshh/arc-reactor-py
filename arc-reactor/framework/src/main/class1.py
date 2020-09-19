from system_files.decorator.component import Component
from src.main.class2 import Class2
from numpy import array
from system_files.service.sysService import SysService
from system_files.service.getAllFiles import FileService
from system_files.decorator.restrict import Restrict

# @Restrict(frameworkOnly=True,access=["system_files,src"])
@Component()
class Class1:
    def __init__(self,_class2:Class2,myList:list):
        # print(myList)
        print ("inside constructor of class 1")
        print(SysService()==SysService())
        FileService()