from system_files.annotation.component import Component
from src.main.class2 import Class2
from numpy import array

@Component()
class Class1:
    def __init__(self,_class2:Class2,myList:list):
        # print(myList)
        print ("inside constructor of class 1")