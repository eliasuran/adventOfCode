data = open("data.txt").readlines()
cards = [card.split(":") for card in data]

copies = {}
for i, card in enumerate(cards):
    copies[i] = 1

for i, card in enumerate(cards):
    numbers = card[1].strip().split("|")
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
