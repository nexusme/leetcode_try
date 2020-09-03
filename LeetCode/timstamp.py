import time
import datetime

timeStamp = 1592901827668 / 1000
timeArray = time.localtime(timeStamp)
otherStyleTime = time.strftime("%Y--%m--%d %H:%M:%S", timeArray)

dateC = datetime.datetime(2020, 6, 23, 16, 43, 47)
new_timestamp = time.mktime(dateC.timetuple())

print(timeStamp)
print(otherStyleTime)
print(new_timestamp)
