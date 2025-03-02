import random
'''
1 for sanke
-1 for water
0 for gun
'''

computer = random.choice([-1,0,1])
you = input("Enter your choice: ")
youDict={"s":1 , "w": -1 , "g":0}

# this dictionary is use to print what you have chosen and what computer chosen
reversedict = {1:"snake" , -1:"water" , 0:"Gun"}

you = youDict[you]
print(f"You chose {reversedict[you]}\ncomputer chose {reversedict[computer]}")

if(computer == you):
    print("Its a draw")

else:
    if(computer == -1 and you == 1):
        print("you win!")    
    elif(computer == -1 and you == 0):
        print("you lost!")   
    elif(computer == 1 and you == -1):
        print("you lost!")
    elif(computer == 1 and you == 0):
        print("you win!")   
    elif(computer == 0 and you == -1):
        print("you win!")   
    elif(computer == 0 and you == 1):
        print("you lost!")              
