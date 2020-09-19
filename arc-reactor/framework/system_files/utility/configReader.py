import configparser,os
from system_files.decorator.component import Component
from collections import namedtuple

@Component()
class ConfigReader:
    TYPE = namedtuple('_ConfigReader', ["NOT_FOUND","DUPLICATE_KEYS"])("NOT_FOUND","DUPLICATE_KEYS")

    def __init__(self,*args, **kwargs):
        self.__config_dict=dict()
        self.__system_env = kwargs.get('sys_env',"default")
        self.__service_env = kwargs.get('env',"default")

    def setConfigForPath(self,config_path):
        self.__config_dict[config_path] = self.__getAllConfig(config_path)
        return self

    def __getAllConfig(self,config_path):
        config_files= os.listdir(config_path)
        config = configparser.RawConfigParser()
        for files in config_files:
            file_path=os.path.join(config_path,files)
            config.read(file_path)
        return config

    def value(self,path):
        try:
            value_list=list()
            for config_key in self.__config_dict.keys():
                if "system_files" in config_key:
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
    
    def __getValue(self,config_key,env,path,value_list):
        try:
            value_list.append(self.__config_dict[config_key].get(env,path))
        except Exception as ex:
            pass