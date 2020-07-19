from system_files.calling import Calling

class Caller2:
    def __init__(self):
        self.test()
    def test(self):
        self.test2()
    def test2(self):
        Calling()
        Calling()