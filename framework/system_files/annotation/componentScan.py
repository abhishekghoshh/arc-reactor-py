import importlib


class ComponentScan:
    def __init__(self,path):
        self.paths=path
        print(path)
        print(type(path))
    def __call__(self,func):
        class_ = self.class_for_name("src.main.class2","Class2")
        print("class name is ",class_)
        print("class object is",class_())
        return func
    def class_for_name(self,module_name,class_name):
        m = importlib.import_module(module_name)
        c = getattr(m, class_name)
        return c