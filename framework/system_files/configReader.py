import configparser,os
from system_files.annotations import singleton
from system_files.annotation.component import Component

@Component()
class ConfigReader:
    def setConfigForPath(self,config_path):
        self.__config_dict[config_path] = __getAllConfig(config_path)

    def __getAllConfig(self,config_path):
        config_files= os.listdir(config_path)
        config = configparser.RawConfigParser()
        for files in config_files:
            file_path=os.path.join(config_path,files)
            config.read(file_path)
        return config