 

import multiprocessing
import subprocess

# To run Friday
def startFriday():
        # Code for process 1
        print("Process 1 is running.")
        from main import start
        start()


if __name__ == '__main__':
        p1 = multiprocessing.Process(target=startFriday)
        p1.start()

        print("system stop")