N=int(input())

source=list(map(int,input().split()))
doubled=[i**2 for i in source]

for x in doubled:
    print(x,end=' ')