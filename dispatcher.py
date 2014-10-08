import random
from workers import WorkerA, WorkerB, WorkerC
from container import Container

class Dispatcher(object):

    def __init__(self, workers):
        self.workers = workers
    
    def dispatch(self):
    
        while True:
            a = random.randint(1, 1000)
            b = random.randint(1, 1000)
            
            num_operation = random.randint(0, 2)
            
            self.workers[num_operation].work(a, b)
            
