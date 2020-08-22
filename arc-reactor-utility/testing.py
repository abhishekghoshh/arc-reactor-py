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