import random
random.randint(1,100)

jacpot= random.randint(1,100)
guess= int(input("Chal Guess Kar"))
counter=1

while guess != jacpot:
    if guess < jacpot:
        print("Guess Higher")
    else:
        print("Guess Lower")

    guess= int(input("Chai Guess Kar"))
    counter+=1
    
print("sahi Jawab")
print("You took ", counter, "attemps")
