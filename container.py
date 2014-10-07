class Container(object):
    def __init__(self):
        self.implementations = {}
        self.instances = {}
 
    def add_component(self, interface, implementation=None):
        self.implementations[interface] = implementation or interface
 
    def get_component(self, interface):
        if interface in self.instances:
            return self.instances[interface]
        if interface not in self.implementations:
            return None
 
        cls = self.implementations[interface]
        instance = self.instances[interface] = cls.__new__(cls)
 
        for key, classvalue in inspect.getmembers(cls):
            if isinstance(classvalue, Inject):
                value = self.getComponent(classvalue.interface)
                setattr(instance, key, value)
 
        instance.__init__()
        return instance

