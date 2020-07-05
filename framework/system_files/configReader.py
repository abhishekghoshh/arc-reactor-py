import configparser,os
class ConfigReader:
    __instance = None
    @staticmethod 
    def getInstance():
        """ Static access method. """
        if ConfigReader.__instance == None:
            ConfigReader()
        return ConfigReader.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if ConfigReader.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            ConfigReader.__instance = self
        
    def getAllConfig(self,):
        config_dir=r"../configs"
        config_files= os.listdir(config_dir)
        print(config_files)
        config = configparser.RawConfigParser()
        for files in config_files:
            file_path=os.path.join(config_dir,files)
            config.read(file_path)
        return config

    def getConfigType(self,data_type):
        return None
