'''

                    datetime
                       |
            --------------------------
           |           |              |
         date         time         datetime  1 level
                                      |
                                       -year()
                                      |
                                       -month()  2nd level
                                      |
                                       - day()

'''

#create datetime
'''
datetime(year,month,day,hour,minut,second)
'''

import datetime

'''
dt1=datetime.datetime(2022,11,21)
print(dt1)

dt2=datetime.datetime(2022,11,21,20,25,45)
print(dt2)
'''

# TO extract system date and time use now() method
sysdt=datetime.datetime.now()
print(sysdt)
y=sysdt.year
print(y)
m=sysdt.month
print(m)
s=sysdt.second
print(s)

hr=sysdt.hour
print(hr)
min=sysdt.minute
print(min)
sec=sysdt.second
print(sec)

