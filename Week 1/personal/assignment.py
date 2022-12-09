print("let's play paper, scissor and rock")
a = 0
b = 0
c = 0
for i in range(5):
    possible_choice =('paper', 'scissor', 'rock')   
    import random 
    computer_choice = random.choice(possible_choice)
    #print(computer_choice)
    user_choice = input("Choose paper or scissor or rock: ")
    if computer_choice == user_choice :
        print("Both choosed same so game is tied.")
        a = a + 1
    elif computer_choice == 'paper' and user_choice == 'scissor':
        print('Human won')
        b = b + 1
    elif computer_choice == 'paper' and user_choice == 'rock':
        print('Computer won')
        c = c + 1
    elif computer_choice == 'scissor' and user_choice == 'rock':
        print('Human won')
        b = b + 1
    elif computer_choice == 'scissor' and user_choice == 'paper':
        print('Computer won')
        c = c + 1
    elif computer_choice == 'rock' and user_choice == 'paper':
        print('Human won')
        b = b + 1
    elif computer_choice == 'rock' and user_choice == 'scissor':
        print('Computer won')
        c = c + 1
a = str(a)
b = str(b)
c = str(c)
print('Therefore Human won ' + b + ' times and computer won ' + c + ' times and ' + a + ' times game is tied.')   