import random 
from random import randint   # randint is function which gives random numbers in particular range 

print("Welcome to the Guess Number Game")
user_name=input('Enter the Name: ').capitalize()
random_num = randint(1,100)
# print(random_num)
guess = ''
guess_limit = 5
guess_chance = 0
out_of_the_chance = False 

while random_num!=guess and not(out_of_the_chance):
    if guess_chance<guess_limit:
        try:
            guess = int(input("Guess a Number: "))
            guess_chance+=1
            if random_num>guess:
                print('too low')
            elif random_num<guess:
                print('too high')
            else:
                print(f'Bingo {user_name} you won')
        except Exception as e :
            print(e)
    else :
        out_of_the_chance=True
if out_of_the_chance:
    print("Out of chances \nyou lose")
    print(f'The answer was {random_num}')
    print(f"{user_name} you lost")



    

