
class StringUtils:
    def __init__(self):
        print(None)

    @staticmethod
    def isStrNotBlank(name_):
        return bool(name_ and name_.strip())

    @staticmethod
    def isString(str_):
        return None!= str_ and type(str_) == str

    @staticmethod
    def stringEqualsIgnoreCase(str1,str2):
        if StringUtils.isString(str1) and StringUtils.isString(str2):
            return str1.lower() == str2.lower()
        else:
            return False

    