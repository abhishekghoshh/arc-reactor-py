import sys,os
import arc_reactor.cli.init.__main__ as init
import arc_reactor.cli.help.argumentNotMatched as noArgumentsMatched
import arc_reactor

def main():
    # print(arc_reactor.__file__)
    args = sys.argv[1:]
    if(args[0] == "init"):
        init.main()
    elif(args[0] == "clean"):
        pass
    elif(args[0] == "start"):
        pass
    elif(args[0] == "update"):
        pass
    elif(args[0] == "test"):
        pass
    elif(args[0]=="help"):
        pass
    else:
        noArgumentsMatched.noArgumentsMatched(args[0])
if __name__ == '__main__':
    main()