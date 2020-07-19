from system_files.calling import Calling

class Caller1:
    def __init__(self):
        Calling()
        self.test()
    def test(self):
        print(Calling()==Calling())