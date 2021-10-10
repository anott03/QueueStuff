## Queue Efficiency Stuff
I was curious to see if a queue implemented as a linked list would be more efficient than a queue implemented on top of a list. My general thinking was that holding references to all the data should be faster than holded copies of the actual data. I didn't think it through though, since any reasonable implementation of a list/array already uses references when taking objects, and in the case of primitive data types, a linked list implemententation of a queue will create a series of unnecessary objects that are eliminated by using a list.
#### The Results
Here are a few of the trials... (though now that I see the flaws in my thinking they aren't really necessary):
```
$ python3 test.py
normal queue:  0.6660662749782205
linked list queue:  1.3351772499736398
$ python3 test.py
normal queue:  0.6657038319390267
linked list queue:  1.347729860106483
$ python3 test.py
normal queue:  0.6666780730010942
linked list queue:  1.3547994869295508
```
The queue implemented with a list is consistently about twice as fast as the linked list implementation.
