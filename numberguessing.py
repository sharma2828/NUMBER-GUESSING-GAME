import random
a=int(input("ENTER THE END NUMBER OF THE RANGE: "))
b=random.randrange(0,a)
print(b)
x=int(input("ENTER THE NUMBER OF CHANCES YOU WANT FOR GUESSING"))
print("NUMBER OF CHANCES YOU GET ARE :",x)
y=0
while True:
    c=int(input("ENTER THE NUMBER YOU GUESSED: "))
    if b==c:
     print("WOW! YOU WON")
     break
    if b>c:
     print("TRY AGAIN!YOU GUESSED A LOWER NUMBER")
     y=y+1
    if b<c:
     print("TRY AGAIN!YOU GUESSED A HIGHER NUMBER")
     y=y+1
    if x==y:
        print("BETTER LUCK NEXT TIME!YOUR CHANCES ARE OVER")
        break
     
 

    
