N=int(input())
total=0

for _ in range(N):
    a,b=map(int,input().split())
    for i in range(a,b+1):
        if i%2==0:
            total+=i
    print(total)
    total=0