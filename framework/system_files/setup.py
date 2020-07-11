from system_files.service import pythonVersion,dependencySetup
import os
from system_files.utility import stopWarning
from system_files.annotations import logger,printNothing

@printNothing
def setup():
    stopWarning()
    pythonVersion()
    checkDependencyOfSrcAndSys()
    
@printNothing
def checkDependencyOfSrcAndSys():
    system_file_path = os.path.join(os.getcwd(),"system_files")
    dependencySetup(system_file_path)
    src_file_path = os.path.join(os.getcwd(),"src")
    dependencySetup(src_file_path)


def StartPythonApplication(func):
    setup()
    return func