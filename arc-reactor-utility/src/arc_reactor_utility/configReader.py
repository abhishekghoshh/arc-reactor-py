import configparser,os
from collections import namedtuple

class ConfigReader:
    def __init__(self):
        pass

    @staticmethod
    def getInstance():
        pass

    TYPE = namedtuple('_ConfigReader', ["NOT_FOUND","DUPLICATE_KEYS"])("NOT_FOUND","DUPLICATE_KEYS")

    def __init__(self,*args, **kwargs):
        self.__config=list()

    def setConfig(self,config_path):
        if(self.__isValidPath(config_path)):
            self.__getAllConfig(config_path)
            return self
        else:
            raise Exception("Not a proper path")

    def __isValidPath(self,path):
        if(None!=path and ""==path.strip()):
            return os.path.exists(path)
        else:
            print("path can not be None")
            return False

    def __getAllConfig(self,config_path):
        for _file in os.listdir(config_path):
            config = configparser.RawConfigParser()
            file_path=os.path.join(config_path,_file)
            config.read(file_path)
            _dict=dict()
            _dict["path"]=config_path
            _dict['name']=_file
            _dict["config"]=config
            self.__config.append(_dict)



    def value(self,path):
        try:
            value_list=list()
            for config_key in self.__config_dict.keys():
                if "system_modules" in config_key:
                    self.__getValue(config_key,self.__system_env,path,value_list)
                else:
                    self.__getValue(config_key,self.__service_env,path,value_list)
            if(len(value_list)==0):
                return ConfigReader.TYPE.NOT_FOUND
            elif(len(value_list)==1):
                return value_list[0]
            else:
                return ConfigReader.TYPE.DUPLICATE_KEYS
        except Exception as ex:
            return ex
    
    # def __getValue(self,config_key,env,path,value_list):
    #     try:
    #         value_list.append(self.__config_dict[config_key].get(env,path))
    #     except Exception as ex:
    #         pass