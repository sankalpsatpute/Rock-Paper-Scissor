import random 

user_choice = int(input("type 0 for rock and 1 for scisor and 2 for paper: "))

computer_choice = random.randint(0,2)
print(f"roy choice is {computer_choice}")

if user_choice >= 3 or user_choice < 0:
    print("You have enter wrong Number. You lose")

elif user_choice == computer_choice:
    print("Draw")
    
elif (user_choice == 0 and computer_choice == 1) or \
     (user_choice == 1 and computer_choice == 2) or \
     (user_choice == 2 and computer_choice == 0):
    print("You win!")

else:
    print("You Lose")
    
    
    
    

         
