from system_files.annotation.component import Component
from src.main.Class3 import Class3

@Component(value=Component.TYPE.SINGLETON)
class Class2:
  def __init__(self,_class3:Class3):
    print("I am in constructor class 2")
    