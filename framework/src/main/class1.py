from system_files.annotations import component
from src.main.class2 import Class2
from numpy import array

@component
class Class1:
    def __init__(self,obj=Class2(),x_=list()):
        self.x_=x_
        self.class2_=obj
        print ("inside constructor of class 1")