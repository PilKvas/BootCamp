i = 0
while i <= 10:
    i = i + 1
    if i > 7:
        i = i + 2

ticket = int(input())

part1 = ticket // 1000
part2 = ticket % 1000

piece1 = part1 % 10
piece2 = part1 // 100
piece3 = (part1 % 100) // 10
sum1 = piece1 + piece2 + piece3

piece1_1 = part2 % 10
piece2_2 = part2 // 100
piece3_3 = (part2 % 100) // 10
sum2 = piece1_1 + piece2_2 + piece3_3

if sum1 == sum2: 
    print("Счастливый")
else: print("Обычный")
