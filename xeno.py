ins = open("xeno","r")
f = file("output","w")
latency = []
for i in range(100):
    latency.append(0) 
for line in ins:
    item = line.strip().split(":")
    if int(item[2]) < 0:
        item[2] = 0
    latency[int(item[2])] = latency[int(item[2])]+1
for i in range(100):
    value = "{:06} {:06}\n".format(i,latency[i])
    f.write(value)
ins.close()
f.close()
