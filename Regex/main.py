import re

f = open('sample.srt', 'r')
string = f.read()
f.close()
p = re.compile('\d\d:\d\d:\d\d,\d\d\d --> \d\d:\d\d:\d\d,\d\d\d\n')
times = p.findall(string)
total = 0
for time in times:
    time = time[0:len(time) - 1]
    time = time.split()
    time1 = int(time[0][0:2]) * 3600 + int(time[0][3:5]) * 60 + int(time[0][6:8]) + int(time[0][9:12]) * 0.001
    time2 = int(time[2][0:2]) * 3600 + int(time[2][3:5]) * 60 + int(time[2][6:8]) + int(time[2][9:12]) * 0.001
    total += time2 - time1
print(total)
