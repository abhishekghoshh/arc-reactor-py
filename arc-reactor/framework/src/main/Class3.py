from system_files.decorator.component import Component
from system_files.decorator.disablePrint import DisablePrint
from system_files.decorator.hystrixHandler import HystrixHandler


@Component(value=Component.TYPE.SINGLETON)
class Class3:
  def __init__(self):
    print("I am in constructor class 3")
    
  @DisablePrint()
  def call(self):
    print("Hey there")

  @HystrixHandler(fallbackMethod="fallback",commandKey="hystrixTest",ignoreExceptions=[],thresoldTimeInMS = 100)
  def hystrixTest(self,x:int,y:int) ->int:
    return x+y
  
  def fallback(self):
    print("I am in fallback")
    
  def myFallback(self):
    print("custom fallback")