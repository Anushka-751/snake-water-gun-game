import random
computer=random.choice([-1,0,1])
youstring=input("Enter ur choice: ");
youdict={"s":1,"w":-1,"g":0}
reversedict={1:"s",-1:"w",0:"g"}
you=youdict[youstring]
print(f"you chose: {reversedict[you]} \ncomputer chose: {reversedict[computer]}")
if(computer == you):
    print("draw") 
else:
    if(computer== -1 and you==1):
        print("You win!")
    elif(computer== -1 and you==0):
        print("You win!")
    elif(computer== 1 and you==-1):
        print("You lose!")
    elif(computer== 1 and you==0):
        print("You win!")
    elif(computer== 0 and you==-1):
        print("You win!")
    elif(computer== 0 and you==1):
        print("You win!")
    else:
        print("Something went wrong")   



