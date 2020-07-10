from system_files.installer import installPip,install
from system_files.packageInfo import IfInstalled,getLocalPackages,checkForLatestPackage
from system_files.getAllFiles import getAllImports
import threading,os,sys



def dependencySetup(path):
    try:
        import pip
    except ImportError:
        print("pip not present.")
        installPip()
    imported_files= getAllImports(path=path)
    if(len(imported_files) != 0):
        all_package_is_istalled=True
        threads = list()
        print(imported_files)
        checkForLatestPackage(imported_files)
        uniInstalledPackages= IfInstalled(imported_files)
        localPackages = getLocalPackages(path)
        for package_ in uniInstalledPackages:
            if package_ not in localPackages:
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



def pythonVersion():
    if sys.version_info.major < 3:
        print('Upgrade to Python 3')
        exit(1)
    else:
        print("Your python version is ",sys.version)