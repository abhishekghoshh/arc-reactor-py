import sys,os
import arc_reactor.cli.init.__main__ as init

# from .classmodule import MyClass
# from .funcmodule import my_function
def main():
    args = sys.argv[1:]
    if(args[0] == "init"):
        init.main()
    
    # print('count of args :: {}'.format(len(args)))
    
    # for arg in args:
    #     print('passed argument :: {}'.format(arg))
    # my_function('hello world')
    # my_object = MyClass('Thomas')
    # my_object.say_name()
if __name__ == '__main__':
    main()