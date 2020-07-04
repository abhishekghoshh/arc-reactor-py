from installer import installPip,IfInstalled
from getAllFiles import getAllImports

def setup(path):
    try:
        import pip
    except ImportError:
        print("Pip not present.")
        installPip()
    imported_files= getAllImports(path=path)
    print(IfInstalled(imported_files))


setup(r"C:\Users\ASUS\Desktop\Python\My project\framework\src")