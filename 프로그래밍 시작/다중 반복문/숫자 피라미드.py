N=int(input())

for i in range(1,N+1):
    for j in range(i,i+1):
        for q in range(0,i):
            print(j,end=' ')
    print()