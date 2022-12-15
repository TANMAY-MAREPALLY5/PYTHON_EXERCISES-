list=[1,3,6,22,55]

max=list[0]
print("Given list:")
for i in list:
    print(i,end=" ")

print()
for i in list:
    if i>max:
        max=i

print(max,"is the largest in the list")
