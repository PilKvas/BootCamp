num1 = int(input())
num2 = int(input())
num3 = int(input())

max1 = max(num1,num2,num3)
min1 = min(num1,num2,num3)
other = (num1 + num2 + num3) - (max1 + min1)

print(max1)
print(min1)
print(other)