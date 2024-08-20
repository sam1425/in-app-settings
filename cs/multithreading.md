why is so difficult?:
* race condition: if you put a thread to say 1 and other thread say 2 each one of the threads will rush to make a update and you have to make a sort of traffic cop
	* you can do it by waiting until the other thread has updated the variable but this causes that the run time is not so different than just one thread

* shared resource: split the resource in the 2 parts 
	* this make another problem come up that is that also the threads are unsynchronized  
	* one solution to this is to do another thread that synchronize the 2 threads and only release when the 2 threads are done