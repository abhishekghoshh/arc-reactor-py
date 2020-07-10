from system_files.installer import installPip,IfInstalled,getLocalFiles,install
from system_files.getAllFiles import getAllImports
import threading,os,sys
import subprocess
import json
import urllib.request


def dependencySetup(path):
    all_package_is_istalled=True
    threads = list()
    try:
        import pip
    except ImportError:
        print("pip not present.")
        installPip()
    imported_files= getAllImports(path=path)
    checkLatestVersionForPackageList = [checkLatestVersionForPackage(package_name) for package_name in imported_files]
    print(checkLatestVersionForPackageList)
    print(imported_files)
    uniInstalledPackages= IfInstalled(imported_files)
    for package_ in uniInstalledPackages:
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

def checkLatestVersionForPackage(package_name):
    checkLatestVersionForPackageObject = dict()
    try:
        latestVersion = checkLatestVersion(package_name)
    except Exception as ex:
        latestVersion="skipped"
    checkLatestVersionForPackageObject[package_name]=latestVersion
    return checkLatestVersionForPackageObject

def pythonVersion():
    if sys.version_info.major < 3:
        print('Upgrade to Python 3')
        exit(1)
    else:
        print("Your python version is ",sys.version)

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