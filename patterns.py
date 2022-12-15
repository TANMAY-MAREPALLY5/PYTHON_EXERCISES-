n=int(input("Enter no of rows:"))

#FIRST PATTERN

for i in range(0,n+1):
    for j in range(0,i):
        print("*",end=" ")
    print()

print("\n")
#SECOND PATTERN

for i in range(n,0,-1):
    for j in range(0,i):
        print("*",end=" ")
    print()

print("\n")
#THIRD PATTERN

for i in range(0,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

print("\n")

#FOURTH PATTERN
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()
