from system_files.service import pythonVersion,checkLatestVersion,dependencySetup
import os


def StartPythonApplication(func):
    pythonVersion()
    newmethod187()
    return func

def newmethod187():
    system_file_path = os.path.join(os.getcwd(),"system_files")
    dependencySetup(system_file_path)
    src_file_path = os.path.join(os.getcwd(),"src")
    dependencySetup(src_file_path)

