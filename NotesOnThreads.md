# Python Threads

See: Python Coockbook 9.2

The threads in python cannot be killed. Instead they need to be implmented in
such way that the thread itself periodically asks if should continue.
This is a "feature" of python that forces you to design the thread carefully.


## Problem:
We need to stop a thread from the outside, but python does not allow a thread
to kill another.

## Solution

We have to implement a mechanism with which we ask the thread to go away. each
thread must periodically check whether it's been asked to go away then clean 
and leave if so.

```python
import threading
class TestThread(threading.Thread):
    def __init__(self, name='TestThread'):
    """ constructor, setting initial variables """
    self._stopevent = threading.Event( )
    self._sleepperiod = 1.0
    threading.Thread.__init__(self, name=name)
    def run(self):
        """ main control loop """
        print "%s starts" % (self.getName( ),)
        count = 0
        while not self._stopevent.isSet( ):
            count += 1
            print "loop %d" % (count,)
            self._stopevent.wait(self._sleepperiod)
        print "%s ends" % (self.getName( ),)
    def join(self, timeout=None):
        """ Stop the thread and wait for it to end. """
        self._stopevent.set( )
        threading.Thread.join(self, timeout)

if __name__ == "__main__":
    testthread = TestThread( )
    testthread.start()
    import time
    time.sleep(5.0)
    testthread.join( )
```

The `TestThread` class overrides `Threading.Thread`s `join` method, normally
`join` waits for a thread to finish without doing anything to cause that 
termination. In this recipe the stop event is set before delegating the rest
of the operation to the base class `join` method.

An alternative implementation would expose the event to make it controllable
from the outside. For example all threads in a pool might stop when one event
object all they share is set.
