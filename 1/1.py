data = open("data.txt").readlines()

sum = 0

for word in data:
    calibrated = []

    for letter in word:
        if letter.isdigit():
            calibrated.append(letter)

    if len(calibrated) == 1:
        calibrated.append(calibrated[0])

    sum += int(calibrated[0] + calibrated[-1])

print(sum)
