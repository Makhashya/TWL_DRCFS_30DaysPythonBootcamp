import random
import string
def fun_rank(password: str) -> str:
    #password = input("Enter password: ")
    length = len(password)
    #print(length)
    #print(password[0])
    val = 0
    capital = 0
    small = 0
    special = 0
    num = 0
    other = 0
    for i in range(length):
        if password[val] >= 'A' and password[val] <= 'Z':
            capital = 1
        elif password[val] >= 'a' and password[val] <= 'z':
            small = 1
        elif password[val] == "!" or password[val] == "+"  or password[val] == "-"  or password[val] == "="  or password[val] == "="  or password[val] == "?"  or password[val] == "#"  or password[val] == "%"  or password[val] == "*"  or password[val] == "@"  or password[val] == "&"  or password[val] == "^"  or password[val] == "$"  or password[val] == "_":
            special = 1
        elif password[val] >= "0" and password[val] <= "9":
            num = 1  
        else:
            other = 1
        val = val + 1

    #print(capital,small,special,num,other)
    sum = 0 
    sum = capital + small + special + num
    sum = int(sum)
    length = int(length)
    #print(sum)
    rank = "invalid"
    if sum == 4 and length >= 10:
        rank = "strong"
    elif sum == 4 and length >=8:
        rank = "moderate" 
    elif sum == 3 and length > 7:
        rank = "moderate"
    else:
        rank = "poor"

    #print(rank)             
    return rank 
def option_1(FILE: str) -> int:
    with open(FILE,'r') as file:
        file1 = open("Week 2\\Assignments\\user-pwds-checked.txt","w")
        password1 = file.readlines()
        print(password1)
        counter = 0
        for val in password1:
            name,password = val.split(",")
            print(password)
            password = password[:-1]
            print(name,password)
            rank = fun_rank(password)
            #print(rank)
            file1.write(name + "," + password + "," + rank+"\n")
            counter = counter + 1
        file1.close()
    return counter

def generate() -> str:
    special = "!+-=?#%*&^$_"
    pc = string.ascii_lowercase + string.ascii_uppercase + special + string.digits
    pa = ''.join(random.choice(pc) for i in range(10))
    #print(pa)
    return pa

def option_2() -> bool:
    length = 25
    while length > 20:
        print("Enter username having less than 20 characters:")
        username = input("Enter username: ")
        length = int(len(username))
        ch = "N"
        while ch == 'N':
            password = generate()
            print("Randomly generated password is:", password)
            opt = input("Do you like to keep password? Y or N: ")
            if opt == "Y":
                with open("Week 2\\Assignments\\user-pwds.txt",'a') as file:
                    file.write(username+","+password)
            ch = opt

def option_3() -> bool:
    print("Thank You\n")
    print("This program is courtesy of: Ujwal Makhashya")
    return 1


print("Welcome to my password ranking program")
print("-"*40)
print("Please select one of 3 options")
print("Option1. Rank password from existing file\t Option2. Generate a strong password \nOption3. Exit the program")
inp = 1
while inp != 3:
    inp = int(input("Enter your option here: "))
    if inp == 1:
        FILE = input("Enter the relative file path: ")
        number = str(option_1(FILE))
        print("The total number of passowrd checked is: "+ number + ". Feedback output can be found in Week 2\\Assignments\\user-pwds-checked.txt")
    elif inp == 2:
        option_2()
    elif inp == 3:
        option_3()
        break
    else:
        print("Please choose option 1, 2 or 3.")

   





    