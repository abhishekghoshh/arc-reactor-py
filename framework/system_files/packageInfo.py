from system_files.utility import stringEqualsIgnoreCase
import subprocess,sys
from system_files.getAllFiles import getAllFIlesName
import subprocess
import json
import urllib.request
from system_files.annotations import logger,printNothing


@printNothing
def checkBothPackageList():
    help("modules")
    all_packages=list()
    reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
    installed_packages_list1 = [r.decode().split('==')[0] for r in reqs.split()]
    all_packages.extend(installed_packages_list1)
    installed_packages_list2 = list(sys.modules.keys())
    all_packages.extend(installed_packages_list2)
    return all_packages

def getLocalPackages(path):
    all_files = getAllFIlesName(path)
    local_files=list()
    for file_ in all_files:
        local_files.append(file_["file_name"].split(".")[0])
    return local_files

def IfInstalled(imported_files):
    installed_packages = checkBothPackageList()
    unInstalled_packages = list(filter(lambda imported_file: (imported_file not in installed_packages) , imported_files))
    return unInstalled_packages

def checkForLatestPackage(imported_files):
    checkLatestPackageEnabled = "N"
    if(stringEqualsIgnoreCase("Y",checkLatestPackageEnabled)):
        checkLatestVersionForPackageList = [checkLatestVersionForPackage(package_name) for package_name in imported_files]
        print(checkLatestVersionForPackageList)

def checkLatestVersionForPackage(package_name):
    checkLatestVersionForPackageObject = dict()
    try:
        latestVersion = checkLatestVersion(package_name)
    except Exception as ex:
        latestVersion="skipped"
    checkLatestVersionForPackageObject[package_name]=latestVersion
    return checkLatestVersionForPackageObject

def checkLatestVersion(name):
    # create dictionary of package versions
    pkgs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
    keys = [p.decode().split('==')[0] for p in pkgs.split()]
    values = [p.decode().split('==')[1] for p in pkgs.split()]
    d = dict(zip(keys, values)) # dictionary of all package versions

    # retrieve info on latest version
    contents = urllib.request.urlopen('https://pypi.org/pypi/'+name+'/json').read()
    data = json.loads(contents)
    latest_version = data['info']['version']

    if d[name]==latest_version:
        print('Latest version (' + d[name] + ') of '+str(name)+' is installed')
        return True
    else:
        print('Version ' + d[name] + ' of '+str(name)+' not the latest '+latest_version)
        return False