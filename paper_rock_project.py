#randint() inbuilt function is used for generating random integer values within the given range.

import random

print('Wining rules of the game Rock,Paper,Scissor are:\n'
      +"Rock vs Paper -> Paper wins \n"
      +"Rock vs Scissor -> Rock wins \n"
      +"Paper vs Scissor -> Scissor wins \n")

while True:
    print("Enter your choice \n 1-Rock \n 2-Paper \n 3-Scissor \n")
    choice=int(input("Enter your choice:"))
    while choice>3 or choice<1:
        print(int(input("Enter valid choce please:")))
    if choice==1:
        choice_name='Rock'
    elif choice==2:
        choice_name='Paper'
    else:
        choice_name='Scissor'

    print("User choice:",choice_name)
    print("Now it's Computer's Turn...")
    comp_choice=random.randint(1,3)
    if comp_choice==1:
        comp_choice_name='Rock'
    elif comp_choice==2:
        comp_choice_name='Paper'
    else:
        comp_choice_name='Scissor'

    print("Computer choice is:",comp_choice_name)
    print(choice_name, 'vs',comp_choice_name)

    if choice==comp_choice:
        result='DRAW'
    elif (choice==1 and comp_choice==2) or (choice==2 and comp_choice==1):
        result='Paper'
    elif (choice==1 and comp_choice==3) or (choice==3 and comp_choice==1):
        result='Rock'
    elif (choice==2 and comp_choice==3) or (choice==3 and comp_choice==2):
        result='Scissor'

    if result=="DRAW":
        print("___It's a Tie___")
    elif result==choice_name:
        print("___User Win___")
    else:
        print("___Computer Win___")

    print("DO YOU WANT TO PLAY AGAIN? (Y/N)")
    ans=input().lower()
    if ans=='n':
        break

print("Thanks For Playing.......")


