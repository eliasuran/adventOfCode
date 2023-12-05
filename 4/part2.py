data = open("data.txt").readlines()

copies = {}
for i, card in enumerate(data):
    copies[i] = 1

for i, card in enumerate(data):
    numbers = card.split(":")[1].strip().split("|")
    matching = 0
    cardSum = 0
    for num in numbers[0].split(" "):
        for yourNum in numbers[1].split(" "):
            if yourNum.isdigit() and num.isdigit():
                if int(yourNum) == int(num):
                    matching += 1
    for j in range(copies[i]):
        for xdd in range(matching):
            copies[i + xdd + 1] += 1
sum = sum(copies.values())
print(sum)
