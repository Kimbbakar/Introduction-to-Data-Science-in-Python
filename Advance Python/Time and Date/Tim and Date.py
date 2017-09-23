import datetime as dt
import time as tm 

print tm.time()

dtnow = dt.datetime.fromtimestamp(tm.time())

print dtnow


delta = dt.timedelta(days = 100)

print delta

today = dt.date.today()


print today

print today - delta