from src.main.class1 import Class1
from src.main.class2 import Class2
from src.main.Class3 import Class3
from src.main.function1 import function1
from system_files.configReader import ConfigReader
import ast
import os

from system_files.annotation.disablePrint import DisablePrint

# @DisablePrint()
def main():
    print("Hello world")
    # class1_obj1= Class1()
    # Class3().call()
    # class1_obj2= Class1()
    # print("both class1 object are same : ",class1_obj1==class1_obj2)
    # class2_obj1= Class2()
    # class2_obj2= Class2()
    # print("both class2 object are same : ",class2_obj1==class2_obj2)
    
    # function1(1,2)    
    path = os.path.join(os.getcwd(),r"system_files\system_config")
    cr = ConfigReader().setConfigForPath(path)
    
    print(type(ast.literal_eval((cr.getAllConfig()[path]).get("default","minimum.version.major"))))