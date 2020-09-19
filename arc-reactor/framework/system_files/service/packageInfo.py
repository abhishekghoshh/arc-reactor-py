from system_files.utility.stringUtils import StringUtils
import subprocess,sys
import json
import urllib.request
from system_files.decorator.component import Component
from system_files.decorator.disablePrint import DisablePrint

@Component()
class PackageInfoService:
    def __init__(self):
        print("PackageInfoService __init__")

    def checkForLatestPackage(self,imported_files):
        checkLatestPackageEnabled = "N"
        if(StringUtils.stringEqualsIgnoreCase("Y",checkLatestPackageEnabled)):
            checkLatestVersionForPackageList = [self.__checkLatestVersionForPackage(package_name) for package_name in imported_files]
            print(checkLatestVersionForPackageList)

    def IfInstalled(self,imported_files):
        installed_packages = self.__checkBothPackageList()
        unInstalled_packages = list(filter(lambda imported_file: (imported_file not in installed_packages) , imported_files))
        return unInstalled_packages

    @DisablePrint()
    def __checkBothPackageList(self):
        help("modules")
        all_packages=list()
        reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
        installed_packages_list1 = [r.decode().split('==')[0] for r in reqs.split()]
        all_packages.extend(installed_packages_list1)
        installed_packages_list2 = list(sys.modules.keys())
        all_packages.extend(installed_packages_list2)
        return all_packages

    def __checkLatestVersionForPackage(self,package_name):
        checkLatestVersionForPackageObject = dict()
        try:
            latestVersion = self.__checkLatestVersion(package_name)
        except Exception as ex:
            latestVersion="skipped"
        checkLatestVersionForPackageObject[package_name]=latestVersion
        return checkLatestVersionForPackageObject

    def __checkLatestVersion(self,name):
        # create dictionary of package versions
        pkgs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
        keys = [p.decode().split('==')[0] for p in pkgs.split()]
        values = [p.decode().split('==')[1] for p in pkgs.split()]
        d = dict(zip(keys, values)) # dictionary of all package versions
        contents = urllib.request.urlopen('https://pypi.org/pypi/'+name+'/json').read()
        data = json.loads(contents)
        latest_version = data['info']['version']

        if d[name]==latest_version:
            print('Latest version (' + d[name] + ') of '+str(name)+' is installed')
            return True
        else:
            print('Version ' + d[name] + ' of '+str(name)+' not the latest '+latest_version)
            return False