#WAP to find the sum of all even and odd number from 1 to 100.
esum=0
osum=0
for x in range(1,101):
    if x%2==0:
        esum+=x
    else:
        osum+=x
print("the sum is=",esum)        
print("the sum is=",osum)
input()
