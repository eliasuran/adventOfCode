import re
data = open("data.txt").readlines()

sum = 0

colors = {
    "red": 12,
    "green": 13,
    "blue":  14,
}

for game in data: 
    possible = True
    id = game[5:8].split(":")[0]

    cubes = re.split('[,;]', game[9:])
    for cube in cubes:
        cube = cube.strip()
        for color in colors:
            if color in cube:
                number = cube.split(" ")[0]
                if number.isdigit() and int(number) > colors.get(color):
                    possible = False

    if possible:
        sum += int(id)


print(sum)
