from system_files.annotation.component import Component

@Component(value=Component.TYPE.SINGLETON)
class Class3:
  def __init__(self):
    print("I am in constructor class 3")