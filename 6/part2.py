data = open("data.txt").readlines()
data = [x.split(":")[1].strip().replace(" ", "") for x in data]
seconds = 0
firstWin = 0
lastWin = 0
while True:
    if seconds * (int(data[0]) - seconds) > int(data[1]):
        if firstWin == 0:
            firstWin = seconds
        else:
            lastWin = seconds
    elif seconds * (int(data[0]) - seconds) < int(data[1]) and firstWin != 0:
        break
    seconds += 1
print(lastWin - firstWin + 1)
