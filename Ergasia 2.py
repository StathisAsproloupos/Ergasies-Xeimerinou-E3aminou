import random
b=int(input("Enter a number:.... Plz If you don't enter a number it's not gonna work --> "))

#I sinartisi
def fibonachi(x):
    i=1
    j=1
    for k in range(x-2):
        tmp=i 
        i=i+j 
        j=tmp 
    return i

t=0

#Elegxos gia to an einai protos i oxi o ari8mos fibonachi
if fibonachi(b)==1 or fibonachi(b)==2:
   print("the given number is a prime number")

if fibonachi(b)!=1 and fibonachi(b)!=2 :
    for i in range(20):
        a=random.randrange(2,fibonachi(b))
        t=t+1
        if (a**fibonachi(b))%fibonachi(b) != a%fibonachi(b):
            print("The given number is not a prime number") 
            break
    
if t==20:
    print("The given number is a prime number")            

#EZZZZZZZ