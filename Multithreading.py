import threading as th
import time as t


def func(s):
    print(f"Sleeping for {s}")
    t.sleep(s)

# t1 = t.perf_counter()
# func(1)
# func(3)
# func(5)
# t2 = t.perf_counter()

t1 = t.perf_counter()
th1 = th.Thread(target=func, args=[5])
th2 = th.Thread(target=func, args=[3])
th3 = th.Thread(target=func, args=[1])
th1.start()
th2.start()
th3.start()

th1.join()
th2.join()
th3.join()
t2 = t.perf_counter()

print(f"Time diff is {t2 - t1}")
# def task():
#     for i in range(3):
#         print("Task Running")
#         t.sleep(2)


# t1 = th.Thread(target=task) # call 
# t1.start() # execute
# t1.join()

# print("Main Thread finished")

# class MyThread(t.Thread):
#     def run(self): # thread ko run krtha hai
#         print("thread is running")



# t1 = MyThread() # object creation
# t1.start() # run method hoga toh woh thread ko run krdega



