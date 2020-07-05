from system_files.setup import StartPythonApplication
from src.main.HelloWorld import hello

@StartPythonApplication
def startApplication():
    hello()

if __name__ == "__main__":
    startApplication()