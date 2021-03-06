#!/usr/bin/python
# --*-- coding:utf-8 --*--

import sys
from operator import itemgetter
dict_ip_count = {}
dict_time_count = {}

for line in sys.stdin:
    line = line.strip()
    time,ip,num = line.split('\t')
    try:
        num = int(num)
        if time in dict_time_count:
          if ip in dict_time_count[time]:

            dict_time_count[time][ip] += num
          else:
            dict_time_count[time][ip] = 1

        else:
          new = {}
          new[ip] =  1
          dict_time_count[time] = new

    except ValueError:
        pass



for key, value in dict_time_count.items():
  count_list = list(value.items())
  count_list.sort(key=lambda x: x[1], reverse=True)
  dict_time_count[key]=count_list[0:3]

# let us sort the time dictionary also
sorted_time = sorted(dict_time_count.items(),key = itemgetter(0))


for key, values in sorted_time:
  print(key)
  for i in values:
    print(i)
