#How not to waste time
import time as t
touch=input("Do you want to hear a secret? Y/N?").lower()
if touch== "y":
    pass
else:
    print('Okay! Have a naice day! ;)')
    exit()
for i in range(10,0,-1):
    print(i)
    t.sleep(1)
print('Hahaha! I just wasted 10 seconds of your time!!')