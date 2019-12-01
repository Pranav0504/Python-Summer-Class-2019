import math
n1=int(input("What is the starting number : "))
n2=int(input("What is the upper number : "))

for i in range(n1,n2+1):
#print(i,": ", i**0.5)
    sqrt = i**0.5
    remainder = (sqrt * 10) % 10
    if (remainder == 0): 
        print(i, "is a perfect square")
