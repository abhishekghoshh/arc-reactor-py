from system_files.annotation.component import Component
from system_files.annotation.disablePrint import DisablePrint


@Component(value=Component.TYPE.SINGLETON)
class Class3:
  def __init__(self):
    print("I am in constructor class 3")
    
  @DisablePrint()
  def call(self):
    print("Hey there")