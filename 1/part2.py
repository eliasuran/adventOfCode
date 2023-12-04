data = open("data.txt").readlines()

sum = 0

wordNumbers = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

for word in data:
    calibrated = []

    for i in range(len(word)):
        if word[i].isdigit():
            calibrated.append(word[i])
        else:
            for key in wordNumbers:
                if key == word[i:i+len(key)]:
                    calibrated.append(wordNumbers.get(key))

    if len(calibrated) == 1:
        calibrated.append(calibrated[0])

    sum += int(calibrated[0] + calibrated[-1])

print(sum)
