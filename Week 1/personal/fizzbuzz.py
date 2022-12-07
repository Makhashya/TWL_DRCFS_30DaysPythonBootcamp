#Program Details.
#divisilbe by 3, print fizz
#divisible by 5, print buzz
#divisible by 3 and 5, print fizzbuzz
#if divisible by non, print the number as it is

# solution
# 1. 
number = input("Enter any number")
number = int(number)
if number%3 == 0 and number%5== 0:
    print("Fizzbuzz")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")
else:
    print("Number is not divisible by 3 or 5")

