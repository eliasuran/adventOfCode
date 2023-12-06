data = open("data.txt").readlines()
data = [x.split(":")[1].strip() for x in data]
time = [x for x in data[0].split(" ") if x.isdigit()]
distance = [x for x in data[1].split(" ") if x.isdigit()]
sum = 1
for i in range(len(time)):
    seconds = 0
    firstWin = 0
    lastWin = 0
    while True:
        if seconds * (int(time[i]) - seconds) > int(distance[i]):
            if firstWin == 0:
                firstWin = seconds
            else:
                lastWin = seconds
        elif seconds * (int(time[i]) - seconds) < int(distance[i]) and firstWin != 0:
            break
        seconds += 1
    sum *= lastWin - firstWin + 1
print(sum)
