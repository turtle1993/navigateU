import time
import sys

def countdown(x):
    count = 0
    while (count < x):
        ncount = x - count
        sys.stdout.write("\r%d " % ncount)
        sys.stdout.flush()
        time.sleep(1)
        count += 1
