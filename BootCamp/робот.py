number = int(input())
num_mod= number % 10
num_mod_div = (number % 100)//10

if num_mod == 1 and num_mod_div != 1:
    print(str(number) + " программист")
elif num_mod == 2  or num_mod == 3 or num_mod == 4:
    print(str(number) + " программиста")
else:print(str(number) + " программистов")     


        
    