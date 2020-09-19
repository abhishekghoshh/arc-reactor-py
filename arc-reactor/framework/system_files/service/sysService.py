import sys,threading,os
from system_files.service.installer import InstallerService
from system_files.service.getAllFiles import FileService
from system_files.service.packageInfo import PackageInfoService
from system_files.decorator.component import Component
from system_files.decorator.restrict import Restrict

@Restrict(frameworkOnly=True,access=["system_files"])
@Component()
class SysService:
    
    def __init__(self,_fileService:FileService,_installerService:InstallerService,_packageInfoService:PackageInfoService):
        print("I am inide SysService init")
        self.fileService=_fileService
        self.installer=_installerService
        self.packageInfoService = _packageInfoService

    def checkInternetAvailable(self):
        pass

    def pythonVersion(self):
        if sys.version_info.major < 3:
            print('Upgrade to Python 3')
            exit(1)
        else:
            print("Your python version is ",sys.version)

    def dependencySetup(self,path):
        imported_files= self.fileService.getAllImports(path=path)
        if(len(imported_files) != 0):
            all_package_is_istalled=True
            threads = list()
            print(imported_files)
            self.packageInfoService.checkForLatestPackage(imported_files)
            uniInstalledPackages= self.packageInfoService.IfInstalled(imported_files)
            localPackages = self.fileService.getLocalPackages(path)
            for package_ in uniInstalledPackages:
                if package_ not in localPackages:
                    print("this package is not downloaded ",package_)
                    all_package_is_istalled=False
                    threads.append(threading.Thread(target=self.installer.install, args=(package_,)))
                    threads[-1].start() # start the thread we just created
            for thread_ in threads:                                                           
                thread_.join()  
            if(all_package_is_istalled):
                print("All packages are already downloaded for path ",path)
            else:
                print("All packages are downloaded path ",path)

    def isPipAvailable(self):
        try:
            import pip
        except ImportError:
            print("pip not present.")
            self.installer.installPip()

   