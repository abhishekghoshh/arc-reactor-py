from installer import installPip,IfInstalled,getLocalFiles
from getAllFiles import getAllImports

def setup(path):
    try:
        import pip
    except ImportError:
        print("Pip not present.")
        installPip()
    imported_files= getAllImports(path=path)
    print(imported_files)
    for package_ in IfInstalled(imported_files):
        print(package_ in getLocalFiles(path))


setup(r"C:\Users\ASUS\Desktop\Python\My project\framework\src")