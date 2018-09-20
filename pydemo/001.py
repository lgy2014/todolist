import time

localtime = time.localtime(time.time())
print ("本地时间为 :", localtime)

t1=time.time()
time.sleep(3)

t2=time.time()

print(round((t2-t1)/60,2))