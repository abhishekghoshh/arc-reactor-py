from system_files.annotation.component import Component

@Component()
class StringUtils:
    def __init__(self):
        print(None)

    @staticmethod
    def isStrNotBlank(self,name_):
        return bool(name_ and name_.strip())

    @staticmethod
    def isString(self,str_):
        return None!= str_ and type(str_) == str

    @staticmethod
    def stringEqualsIgnoreCase(self,str1,str2):
        if isString(str1) and isString(str2):
            return str1.lower() == str2.lower()
        else:
            return False

    