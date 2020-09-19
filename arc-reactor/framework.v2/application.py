from arc_reactor.decorator.startArcReactorApplication import StartArcReactorApplication
from src.main.main import main




@StartArcReactorApplication()
def StartArcReactor():
    main()













if __name__ == "__main__":
    StartArcReactor()