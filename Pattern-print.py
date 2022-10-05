n = int(input("enter a num of rows : "))

for i in range(1,n+1):
    for j in range(1,n+1):
        print(i, end=' ')
    print()

print('--------------------------------')

for i in range(1,n+1):
    for j in range(1,i+1):
        print(j, end=' ')
    print()

print('--------------------------------')

for i in range(1,n+1):
    print(" "*(n-i), end=" ")
    print('* '*i)

print('--------------------------------')

for i in range(1,n+1):
    print(" "*(n-i), end=" ")
    print('* '*i)

for i in range(1,n+1):
    if i==1:
        continue
    print(" "*(n-i), end=" ")
    print('* '*i)

for i in range(1,n+1):
    print(" "*2, end=" ")
    print('* '*3)
