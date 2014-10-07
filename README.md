dispatchersandworkers
=====================

Dispatcher and workers solution


Preliminary

I have developed my solution in a python way. I have decided to work with python because it is more confortable for me than with other language and it has been a interesting challenge solve the problem in a pythonic way.

It has been necessary to change some exercise requirements:
- I can´t use Spring, so I have implemented a Dependency injection solution (class Container).
- I haven't use Hibernate. Instead of I use SQLAlchemy like a similar solution for persist objects in a relation database.
  
Code organization

dispatcher.py - Contain dispatcher class definition.
workers.py - Contain three type of worker classes and Worker parent class.
container.py - Contain Container class for Dependency injection solution.
persistence.py - Contain three decorator classes that implement DB storing for worker objects
main.py - Script for init application

Asynchronous solution

Firstly we will need to define one process for each element of service:
- One process that will produce requests for workers (dispatcher).
- One process for each worker which will consume requests, produce results and store them in DB.

All processes will work at the same time, therefore we will need a common structure to communicate dispatcher with workers. Python provides multiprocessing module for this purpose. For example, we can use a Queue object. Dispatcher will write requests in the queue and workers will read from the queue to produce results.

Python queue implementation is only a simple solution. If we can get a better performance, for example, it is possible implements  a queue using a key-value DB like Redis
