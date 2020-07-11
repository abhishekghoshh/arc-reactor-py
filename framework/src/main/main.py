from src.main.class1 import class1
from src.main.class2 import class2
from src.main.function1 import function1

def main():
    print("Hello world")
    class1_obj1= class1()
    class1_obj2= class1()
    print("both class1 object are same : ",class1_obj1==class1_obj2)
    class2_obj1= class2()
    class2_obj2= class2()
    print("both class2 object are same : ",class2_obj1==class2_obj2)
    
    function1()