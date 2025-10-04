N=int(input())
num=101-N

for i in range(num):
    if N>=90:
        print("A",end=' ')
    elif N>=80:
        print("B",end=' ')
    elif N>=70:
        print("C",end=' ')
    elif N>=60:
        print("D",end=' ')
    else:
        print("F",end=' ')
    N=N+1