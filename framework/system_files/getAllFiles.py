import os
def getAllImports(*args, **kwargs):
    try:
        path = kwargs.get('path', None)
        file_list = getAllFIlesName(path)
        import_set= set()
        for item in file_list:
            getImportStatementFromFile(import_set,item)
        return list(import_set)
    except Exception as ex:
        return ex

def getAllFIlesName(path):
    try:
        file_and_path_list=list()
        getAllFiles(file_and_path_list,path)
        return file_and_path_list
    except Exception as ex:
        return ex 

def getImportStatementFromFile(import_set,item):
    try:
        file_path=item["file_path"]
        content= open(file_path,"r")
        checkFile(import_set,content)
    except Exception as ex:
        return ex   

def addToList(file_and_path_list,item,new_path):
    try:
        if(checkFileIsPy(item)):
            file_and_path_object=dict()
            file_and_path_object["file_name"]=item
            file_and_path_object["file_path"]=new_path
            file_and_path_list.append(file_and_path_object)
    except Exception as ex:
        print(ex)
        return ex

def checkFileIsPy(item):
    try:
        file_type=item.split(".")[-1]
        return file_type == "py"
    except Exception as ex:
        print(ex)
        return False

def getAllFiles(file_and_path_list,path):
    all_item=os.listdir(path)
    for item in all_item:
        new_path= os.path.join(path,item)
        if(os.path.isdir(new_path)):
            getAllFiles(file_and_path_list,new_path)
        else:
            addToList(file_and_path_list,item,new_path)  
def checkImportLine(line):
    try:
        if "from" in line:
            return True
        elif "import" in line:
            return True
        else:
            return False
    except Exception as ex:
        print(ex)
        return False

def addToImportSet(import_set,import_line):
    try:
        import_line_split = import_line.strip().split(" ")
        if "from" == import_line_split[0]:
            word_list=import_line_split[1]
            import_set.add(word_list.split(".")[0])
        if "import" == import_line_split[0]:
            word_list_split=import_line_split[1].split(",")
            for word_list in word_list_split:
                import_set.add(word_list.split(".")[0])
    except Exception as ex:
        return ex

def checkFile(import_set,content):
    try:
        content_list=content.read().strip().split("\n")
        import_line_list = list(filter(lambda line: (checkImportLine(line)) , content_list)) 
        for import_line in import_line_list:
            addToImportSet(import_set,import_line)
    except Exception as ex:
        return ex
