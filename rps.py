import random 

player2=input("What is your name? ")

print("Here are your options: ")
options=['rock','paper','scissors']
for option in options: 
    print(option)
computer_choice= random.choice(options)
person_choice=input(f'{player2.title()} please choose an option: ')
print(f"You chose {person_choice}, We chose {computer_choice}. \n")
    
if computer_choice == person_choice:
     result="We have a draw"
elif computer_choice == 'rock':
       if person_choice == 'scissors':
            result="Computer won!"
       else:
            result=f"{player2.title()} won!"
elif computer_choice == 'scissors':
       if person_choice == 'paper':
            result="Computer won!"
       else:
            result=f"{player2.title()} won!"
elif computer_choice == 'paper':
       if person_choice == 'rock':
            result="Computer won!"
       else:
            result=f"{player2.title()} won!"
print(result)
session_over= False
while not session_over:
    play_again= input("Would you like to play another round? y/n  ")
    if play_again == 'y':
        print("Here are your options: ")
        options=['rock','paper','scissors']
        for option in options: 
                print(option)
        computer_choice= random.choice(options)
        person_choice=input(f'{player2.title()} please choose an option: ')
        print(f"You chose {person_choice}, We chose {computer_choice}. \n")
                
        if computer_choice == person_choice:
            result="We have a draw"
        elif computer_choice == 'rock':
            if person_choice == 'scissors':
                 result="Computer won!"
            else:
                 result=f"{player2.title()} won!"
        elif computer_choice == 'scissors':
            if person_choice == 'paper':
                 result="Computer won!"
            else:
                 result=f"{player2.title()} won!"
        elif computer_choice == 'paper':
            if person_choice == 'rock':
                 result="Computer won!"
            else:
                 result=f"{player2.title()} won!"
        print(result)
    else:
        session_over=True


