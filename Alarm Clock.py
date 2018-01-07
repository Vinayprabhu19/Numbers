# simulate Alarm clock
import time
s =int(input("Enter the number of seconds after which the Alarm has to be triggered"))
print("Alarm Started")
while s != 0:
    time.sleep(1)
    s-=1
    print(s)
print("Alarm Complete")