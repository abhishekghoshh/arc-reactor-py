import inspect
from system_files.decorator.restrict import Restrict
from system_files.decorator.component import Component
@Restrict()
@Component()
class Calling:
    def __init__(self):
        pass