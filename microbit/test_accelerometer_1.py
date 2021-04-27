# Add your Python code here. E.g.
from microbit import *
import utime

test = []
for i in range (0,5):
    currentAcc = accelerometer.get_x()
    test.append(currentAcc)
    utime.sleep(0.05)
    i += 1

print(test)