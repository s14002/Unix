import datetime

f = open('access.log.1')
lines  = f.read().split('\n')
f.close()

i = 0
max_size = len(lines) -1


while i < max_size:
    line = lines[i]
    rdata = line[14:]
    date = float(line[0:13])
    dateTime = datetime.datetime.fromtimestamp(date)
    print str(dateTime) + rdata
    i += 1




