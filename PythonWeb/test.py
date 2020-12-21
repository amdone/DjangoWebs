import time, datetime

acfun = 1605372150404
bili = 1439397556
tw = '2020-11-12T13:48:50.000Z'


twtimeArray = time.strptime(tw.split('.')[0], "%Y-%m-%dT%H:%M:%S")
timeStamp = int(time.mktime(twtimeArray))
print(timeStamp)
acfun = int(acfun/1000)
print(acfun)