import random
from workers import WorkerA, WorkerB, WorkerC
from container import Container

class Dispatcher(object):

    def __init__(self, container):
        self.container = container
    
    def dispatch(self):
    
        while True:
            a = random.randint(1, 1000)
            b = random.randint(1, 1000)
            
            num_operation = random.randint(1, 3)
            
            operation = {1:WorkerA, 2:WorkerB, 3:WorkerC}[num_operation]
            
            worker = self.container.get_component(operation).work(a, b)
            
