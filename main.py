from container import Container
from workers import WorkerA, WorkerB, WorkerC
from dispatcher import Dispatcher

def main ():
    container = container.Container()
    
    worker_A = WorkerA()
    container.add_component(worker_A)
    worker_B = WorkerB()
    container.add_component(worker_B)
    worker_C = WorkerC()
    container.add_component(worker_C)
    
    dispatcher = Dispatcher(container)
    container.add_component(dispatcher)
    
    container.get_component(Dispatcher).dispatch()


if __name__ == "__main__":
    main()
