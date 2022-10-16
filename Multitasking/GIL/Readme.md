# Global Interpreter Lock
The Python Global Interpreter Lock or GIL, in simple words, is a mutex (or a lock) that allows only one thread to hold the control of the Python interpreter.


### Reference Counting
It means that objects created in Python have a reference count variable that keeps track of the number of references that point to the object.


```python
import sys
a = []
b = a
print(sys.getrefcount(a))
```

    3
    

The problem was that this reference count variable needed protection from race conditions where two threads increase or decrease its value simultaneously.\
### Multiple Locks
One way is by adding locks to all data structures that are shared across threads but dding a lock to each object or groups of objects means multiple locks will exist which can cause another problem—Deadlocks (deadlocks can only happen if there is more than one lock). Another side effect would be decreased performance caused by the repeated acquisition and release of locks.\
### Single Lock
The GIL is a single lock on the interpreter itself which adds a rule that execution of any Python bytecode requires acquiring the interpreter lock. This prevents deadlocks (as there is only one lock) and doesn’t introduce much performance overhead. But it effectively makes any CPU-bound Python program single-threaded.

## The Impact on Multi-Threaded Python Programs
A typical python program will either be CPU-bound or I/O bound in their performance.\
**CPU-bound** programs are those that are pushing the CPU to its limit like matrix multiplication, imaghe processing.\
**I/O-bound** programs are the ones that spend time waiting for Input/Output\



```python
# single_threaded.py
import time
from threading import Thread

COUNT = 50000000

def countdown(n):
    while n>0:
        n -= 1

start = time.time()
countdown(COUNT)
end = time.time()

print('Time taken in seconds -', end - start)
```

    Time taken in seconds - 3.866689443588257
    


```python
# multi_threaded.py
import time
from threading import Thread

COUNT = 50000000

def countdown(n):
    while n>0:
        n -= 1

t1 = Thread(target=countdown, args=(COUNT//2,))
t2 = Thread(target=countdown, args=(COUNT//2,))

start = time.time()
t1.start()
t2.start()
t1.join()
t2.join()
end = time.time()

print('Time taken in seconds -', end - start)
```

    Time taken in seconds - 3.5445520877838135
    

As we can see, both versions take almost same amount of time to finish. In the multi-threaded version the GIL prevented the CPU-bound threads from executing in parellel.\
The GIL does not have much impact on the performance of I/O-bound multi-threaded programs as the lock is shared between threads while they are waiting for I/O. But a program whose threads are entirely CPU-bound would not only become single threaded due to the lock but will also see an increase in execution time


### Improvement in the GIL
We discussed the impact of GIL on “only CPU-bound” and “only I/O-bound” multi-threaded programs but what about the programs where some threads are I/O-bound and some are CPU-bound? In such programs, Python’s GIL was known to starve the I/O-bound threads by not giving them a chance to acquire the GIL from CPU-bound threads.\
This was because of a mechanism built into Python that forced threads to release the GIL after a fixed interval of continuous use and if nobody else acquired the GIL, the same thread could continue its use.\ 
The problem in this mechanism was that most of the time the CPU-bound thread would reacquire the GIL itself before other threads could acquire it. This problem was fixed in Python 3.2 in 2009 by Antoine Pitrou who added a mechanism of looking at the number of GIL acquisition requests by other threads that got dropped and not allowing the current thread to reacquire GIL before other threads got a chance to run.


```python
import sys
print(sys.getswitchinterval())
```

    0.005
    

# How to Deal With Python’s GIL

## Multi-processing vs multi-threading 
The most popular way is to use a multi-processing approach where you use multiple processes instead of threads. Each Python process gets its own Python interpreter and memory space so the GIL won’t be a problem.\
The below code would not run in the jupyter notebook. Run the multiprocessing_example.py and the other scripts for fair comparison.
Below are the results:-
1. Single threaded- 3.331
2. Multi threaded- 4.614
3. Mutliprocessing- 2.6724

The time didn’t drop to half of what we saw above because process management has its own overheads. Multiple processes are heavier than multiple threads, so, keep in mind that this could become a scaling bottleneck. 


```python
# from multiprocessing import Pool
# import time

# COUNT = 50000000
# def countdown(n):
#     while n>0:
#         n -= 1


# pool = Pool(processes=2)
# start = time.time()
# r1 = pool.apply_async(countdown, [COUNT//2])
# r2 = pool.apply_async(countdown, [COUNT//2])
# pool.close()
# pool.join()
# end = time.time()
# print('Time taken in seconds -', end - start)
```

# References
1. GIL- https://realpython.com/python-gil/
