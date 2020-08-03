from pyzip import PyZip
from pyfolder import PyFolder
import os


def updateFrameworkZipData():
    try:
        frameworkPath = os.path.join(os.getcwd(),"framework.v2")
        pyzip = PyZip(PyFolder(frameworkPath, interpret=False))
        destinationPath = os.path.join(os.getcwd(),r"src\arc_reactor\cli\init\frameworkZip.py")
        f = open(destinationPath, "w")
        f.write("frameworkZipData="+str(pyzip.to_bytes()))
        f.close()
    except Exception as ex:
        print(ex)
        raise ex

updateFrameworkZipData()