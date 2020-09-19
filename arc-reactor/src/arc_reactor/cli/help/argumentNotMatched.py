from colorama import init,Fore, Back, Style
import sys


def noArgumentsMatched(arg):
    init()
    print(Fore.RED + 'The specified command '+arg+' is invalid. For a list of available options,')
    print(Fore.RED + 'init,start,clean,test,update,help')
    print(Fore.GREEN + "For more detailed help run arc-reactor [command-name] --help")
    print(Style.RESET_ALL)