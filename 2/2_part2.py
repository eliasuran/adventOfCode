import re
data = open("data.txt").readlines()

sum = 0

for game in data: 
    highest = {
        "red": 0,
        "green": 0,
        "blue": 0
    }

    cubes = re.split('[,;]', game.split(":")[1])
    for cube in cubes:
        cube = cube.strip()
        for color in highest:
            if color in cube:
                number = cube.split(" ")[0]
                if number.isdigit() and int(number) > highest[color]:
                    highest[color] = int(number)

    power = int(highest["red"] * highest["green"] * highest["blue"])

    sum += power

print(sum)
