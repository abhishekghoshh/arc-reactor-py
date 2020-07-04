from installer import installPip
from getAllFiles import getAllImports

def setup(path):
    try:
        import pip
    except ImportError:
        print("Pip not present.")
        installPip()
    print(getAllImports(path=r"C:\Users\ASUS\Desktop\Python\My project\framework\src"))

setup("")