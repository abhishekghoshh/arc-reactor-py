from system_files.decorator.component import Component
from system_files.decorator.disablePrint import DisablePrint


@Component(value=Component.TYPE.PROTOTYPE)
class Class3:
  def __init__(self):
    print("I am in constructor class 3")
    
  @DisablePrint()
  def call(self):
    print("Hey there")