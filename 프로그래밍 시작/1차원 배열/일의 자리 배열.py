first=list(map(int,input().split()))

for i in range(8):
    first.append((first[i]+first[i+1])%10)

for x in first:
    print(x,end=' ')