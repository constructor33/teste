import random
import time

n1 = 0
n2 = 0
signe = 0

print("je suis la calculatrice")
n1 = int(input("dit un nombre : " ))
signe = input("dit un signe : ")
n2 = int(input("dit un nombre : "))

if signe == '+' :
    print(n1 + n2)
elif signe == '-' :
    print(n1 - n2)
elif signe == '*' :
    print(n1 * n2)
elif signe == '/' :
    print(n1 / n2)