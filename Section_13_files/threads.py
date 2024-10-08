import time
from threading import Thread

def ask_user():
    start = time.time()
    user_input = input("Please enter your name: ")
    greet = f'Hello{user_input}'
    print(greet)
    print(f'ask_user, {time.time() - start}')

def complex_calculation():
    start = time.time()
    print("Started calculating")
    [x**2 for x in range (20000000)]
    print(f'complex calculation, {time.time() - start}')

start = time.time()
ask_user()
complex_calculation()
print(f'SinglethreatotalTime: {time.time() - start}')

thread1 = Thread(target=complex_calculation)
thread2 = Thread(target=ask_user)

start = time.time()
thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(f'TwoThreadtotalTime: {time.time() - start}')


"""==========Alternative to Threads Module ================="""

from concurrent.futures import ThreadPoolExecutor
"""
Runs multiple threads at once 
"""
with ThreadPoolExecutor(max_workers=2) as pool:
    pool.submit(complex_calculation)
    pool.submit(ask_user)

"""
Only Needed without the "With" context manager
pool.shutdown()
"""