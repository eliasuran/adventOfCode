data = open("data.txt").readlines()
data = [x.strip("\n") for x in data]
instructions = data[0]
map = data[2:]
totalSteps = 0
step = "AAA"
while True:
    if step == "ZZZ":
        break
    for i in range(len(instructions)):
        print(step)
        if step == "ZZZ":
            break
        totalSteps += 1
        current = 0
        for j in range(len(map)):
            if map[j][0:3] == step:
                current = j
                break
        if instructions[i] == "L":
            step = map[current][7:10]
        else:
            step = map[current][12:15]
print(totalSteps)
