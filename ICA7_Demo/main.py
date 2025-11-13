import time
import threading
import random

globalvar = 99
outhouse = threading.Lock()

print('Starting...')
time.sleep(1.55) # sleep for 1550 ms or 1.55 s
print('Done')
print(time.time())
now = time.time()
while (time.time() - now < 2.5):
    time.sleep(0.1)
    print('.', end='')
print()

def SampleThread(c):
    global globalvar#, outhouse
    exitNum = random.randint(10,20)
    print(f"[{exitNum}]")
    while True:
        time.sleep(0.3)
        with outhouse:
            #critical protection section
            globalvar += 3
            print("GlobalVar: ", globalvar)
        currNum = random.randint(10, 20)
        print(f".{c}{currNum}.", end="")
        if exitNum == currNum :
            break
        print('!')
kw = {'c':'A'}
thr = threading.Thread(target=SampleThread, daemon=True, kwargs=kw)
thr.start()
print('Thread Started:')
thr2 = threading.Thread(target=SampleThread, daemon=True, args=['B'])
thr2.start()
print('Thread2 Started:')
if True:
    time.sleep(1)
    print("Main working")
thr.join() #this means we wait for the daemon thread to end
thr2.join()
print('Main Done')
