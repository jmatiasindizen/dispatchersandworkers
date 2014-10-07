from persistence import persistenceA, persistenceB, persistenceC

class Worker(object):
    def __init__(self):
        self.name = ''
        
    def work (self, a, b):
        raise Exception('Not implemented yet')
        
class WorkerA(Worker):
    def __init__(self):
        Worker.__init__()
        
    @persistenceA        
    def work (self, a, b):
        self.result = a + b
    
class WorkerB(Worker):
    def __init__(self):
        Worker.__init__()
    
    @persistenceB      
    def work (self, a, b):
        self.result = a * b
        
class WorkerC(Worker):
    def __init__(self):
        Worker.__init__()
    
    @persistenceC        
    def work (self, a, b):
        if a < b:
            raise Exception('Operation not allowed')
        self.result = a / b

        
