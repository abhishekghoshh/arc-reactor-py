import os
from system_files.decorator.component import Component
from system_files.decorator.restrict import Restrict

@Restrict(frameworkOnly=True,access=["system_files","src"])
@Component()
class FileService:
    def __init__(self):
        print("I am inside Fileservice init")

    def getAllImports(self,*args, **kwargs):
        try:
            path = kwargs.get('path', None)
            if(path!= None):
                file_list = self.__getAllFIlesName(path)
                import_set= set()
                for item in file_list:
                    self.__getImportStatementFromFile(import_set,item)
                return list(import_set)
            else:
                raise Exception("Please ")
        except Exception as ex:
            return ex

    def getLocalPackages(self,path):
        all_files = self.__getAllFIlesName(path)
        local_files=list()
        for file_ in all_files:
            local_files.append(file_["file_name"].split(".")[0])
        return local_files

    def __getAllFIlesName(self,path):
        try:
            file_and_path_list=list()
            self.__getAllFiles(file_and_path_list,path)
            return file_and_path_list
        except Exception as ex:
            return ex 

    def __getImportStatementFromFile(self,import_set,item):
        try:
            file_path=item["file_path"]
            content= open(file_path,"r")
            self.__checkFile(import_set,content)
        except Exception as ex:
            return ex   

    def __addToList(self,file_and_path_list,item,new_path):
        try:
            if(self.__checkFileIsPy(item)):
                file_and_path_object=dict()
                file_and_path_object["file_name"]=item
                file_and_path_object["file_path"]=new_path
                file_and_path_list.append(file_and_path_object)
        except Exception as ex:
            print(ex)
            return ex

    def __checkFileIsPy(self,item):
        try:
            file_type=item.split(".")[-1]
            return file_type == "py"
        except Exception as ex:
            print(ex)
            return False

    def __getAllFiles(self,file_and_path_list,path):
        all_item=os.listdir(path)
        for item in all_item:
            new_path= os.path.join(path,item)
            if(os.path.isdir(new_path)):
                self.__getAllFiles(file_and_path_list,new_path)
            else:
                self.__addToList(file_and_path_list,item,new_path)  
                
    def __checkImportLine(self,line):
        try:
            if "from " in line:
                return True
            elif "import " in line:
                return True
            else:
                return False
        except Exception as ex:
            print(ex)
            return False

    def __addToImportSet(self,import_set,import_line):### modification needed
        try:
            import_line_split = import_line.strip().split(" ")
            if "from" == import_line_split[0]:
                word_list=import_line_split[1]
                import_set.add(word_list.split(".")[0].strip())
            if "import" == import_line_split[0]:
                if("," in import_line):
                    word_list_split=import_line.strip().strip("import").strip().split(",")
                    for word_list in word_list_split:
                        import_set.add(word_list.split(".")[0].strip())
                else:
                    word_list=import_line_split[1]
                    import_set.add(word_list.split(".")[0].strip())
        except Exception as ex:
            return ex

    def __checkFile(self,import_set,content):
        try:
            content_list=content.read().strip().split("\n")
            import_line_list = list(filter(lambda line: (self.__checkImportLine(line)) , content_list)) 
            for import_line in import_line_list:
                self.__addToImportSet(import_set,import_line)
        except Exception as ex:
            return ex
