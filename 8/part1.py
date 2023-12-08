data = open("data.txt").readlines()
data = [x.strip("\n") for x in data]
instructions = data[0]
map = data[2:]
found = False
totalSteps = 0

while not found:
    step = "AAA"
    for i in range(len(instructions)):
        totalSteps += 1
        if instructions[i] == "L":
            print("xp")


print(totalSteps)
