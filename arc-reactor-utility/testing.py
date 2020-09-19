from src.arc_reactor_utility.folder import Folder
import os
import shutil

def action(arguments):
    print(arguments)

myFolder = Folder("")
myFolder.actionForPathAndFile(
    path= myFolder.getPath(),
    actionForFile = action,
    actionForFolder= action,
    argumentForFile={},
    argumentForFolder={}
    )
myFolder.removePyCache()

path = r'C:\Users\ASUS\Desktop\milestone\a18c30c3-7cf0-41f8-baac-4824a86c8fd4'

print(myFolder.typesAvailable(path=path))
print(myFolder.typesAvailable())