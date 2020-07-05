from system_files.installer import installPip,IfInstalled,getLocalFiles,install
from system_files.getAllFiles import getAllImports
from system_files.utility import blockPrint,enablePrint
import threading,os

def dependencySetup(path):
    all_package_is_istalled=True
    threads = list()
    try:
        import pip
    except ImportError:
        print("pip not present.")
        installPip()
    imported_files= getAllImports(path=path)
    print(imported_files)
    for package_ in IfInstalled(imported_files):
        if package_ not in getLocalFiles(path):
            print("this package is not downloaded ",package_)
            all_package_is_istalled=False
            threads.append(threading.Thread(target=install, args=(package_,)))
            threads[-1].start() # start the thread we just created
    for thread_ in threads:                                                           
        thread_.join()  
    if(all_package_is_istalled):
        print("All packages are already downloaded for path ",path)
    else:
        print("All packages are downloaded path ",path)



def StartPythonApplication(func):
    system_file_path = os.path.join(os.getcwd(),"system_files")
    dependencySetup(system_file_path)
    src_file_path = os.path.join(os.getcwd(),"src")
    dependencySetup(src_file_path)
    return func

