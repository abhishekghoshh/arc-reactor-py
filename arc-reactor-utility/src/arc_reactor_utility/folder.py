import os,shutil
from collections import namedtuple

class Folder:
    __permitted_arguments_data_types =[dict,list,type(None)]
    __permitted_action_types =["<class 'function'>","<class 'method'>",str(type(None))]
    __content_exception=['System Volume Information','$RECYCLE.BIN']
    TYPE = namedtuple('_folder', ['FILE','FOLDER'])('FILE','FOLDER')

    def __init__(self,*args, **kwargs):
        self.root_folder = kwargs.get('path',None)
        self.__whole_path=None
        self.__inside_workspace = False
        self.__direct_folder_path = False
        self.__isAfolder()

    def __isAfolder(self):
        if(None!=self.root_folder):
            try:
                self.__direct_folder_path = self.__isValidPath(self.root_folder)
                if(self.__direct_folder_path):
                    self.__whole_path=self.root_folder
                    return None
                self.__inside_workspace = self.__isValidPath(self.__joinPath(os.getcwd(),self.root_folder))   
                self.__whole_path = self.__joinPath(os.getcwd(),self.root_folder)
            except Exception as ex:
                print(ex)
                raise ex
        else:
            self.root_folder=""
            self.__whole_path = os.getcwd()

    def __isValidPath(self,path):
        return os.path.exists(path)
    
    def __joinPath(self,root_path,sub_path):
        try:
            path = os.path.join(root_path,sub_path)
            if(not self.__isValidPath(path)):
                raise Exception("not a valid path")
            return path
        except Exception as ex:
            print(ex)
            raise ex
        

    def setPath(self,path):
        self.root_folder = path
        self.__isAfolder()
    
    def getPath(self):
        return self.__whole_path

    def actionForPathAndFile(self,*args, **kwargs):
        path = kwargs.get('path',None)
        actionForFile = kwargs.get('actionForFile',None)
        argumentForFile = kwargs.get('argumentForFile',None)
        actionForFolder = kwargs.get('actionForFolder',None)
        argumentForFolder = kwargs.get('argumentForFolder',None)
        if(None!=path or self.__isValidPath(path)):
            try:
                self.__checkFunctionAndArguments(actionForFile,argumentForFile,actionForFolder,argumentForFolder)
                self.__actionForPathAndFile(path,actionForFile,argumentForFile,actionForFolder,argumentForFolder)
            except Exception as ex:
                print(ex)
                raise ex   
        else:
            raise Exception("not a valid path")

    def __checkFunctionAndArguments(self,actionForFile,argumentForFile,actionForFolder,argumentForFolder):
        if(not self.__ifPermittedActionTypes(actionForFile)  or not self.__ifPermittedActionTypes(actionForFolder)):
            raise Exception("action should be a function type check Folder.help()")
        if(not self.__ifPermittedArgumentDataType(argumentForFile) or not self.__ifPermittedArgumentDataType(argumentForFolder)):
            raise Exception("argument should be a dict type check Folder.help()")

    def __ifPermittedActionTypes(self,action):
        return str(type(action)) in Folder.__permitted_action_types

    def __ifPermittedArgumentDataType(self,argument):
        return type(argument) in Folder.__permitted_arguments_data_types

    def __actionForPathAndFile(self,path,actionForFile,argumentForFile,actionForFolder,argumentForFolder):
        for content in os.listdir(path):
            if content in Folder.__content_exception:
                continue
            content_path = self.__joinPath(path,content)
            if(os.path.isdir(content_path)):
                try:
                    if(None!=actionForFolder):
                        actionForFolder(self.__setupArguments(content,content_path,argumentForFolder,Folder.TYPE.FOLDER))
                except Exception as ex:
                    print("exception generated for :",content,content_path,ex)
                if(self.__isValidPath(content_path)):
                    self.__actionForPathAndFile(content_path,actionForFile,argumentForFile,actionForFolder,argumentForFolder)
                else:
                    print("path does not exist more ->",content_path)
            elif(os.path.isfile(content_path)):
                try:
                    if(None!=actionForFile):
                        actionForFile(self.__setupArguments(content,content_path,argumentForFile,Folder.TYPE.FILE))
                except Exception as ex:
                    print("exception generated for :",content,content_path,ex)
    
    def __setupArguments(self,content,content_path,argument,fileOrFolder):
        arguments = dict()
        arguments['name']=content
        arguments['path']=content_path
        arguments['isFile'] = fileOrFolder is Folder.TYPE.FILE
        arguments['isFolder'] = fileOrFolder is Folder.TYPE.FOLDER
        arguments['argument']=argument
        return arguments

    @staticmethod
    def help():
        print("help")           

    def removePyCache(self,*args, **kwargs):
        path = kwargs.get('path',os.getcwd())
        self.actionForPathAndFile(
            path=path,
            actionForFolder= self.__removePyCache
        )
    
    def __removePyCache(self,arguments):
        if(arguments['name']=='__pycache__'):
            shutil.rmtree((arguments['path']))