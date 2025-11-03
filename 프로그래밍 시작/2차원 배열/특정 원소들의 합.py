matrix=[list(map(int,input().split())) for _ in range(4)]

total=0
cnt=0

for row in matrix:
    cnt+=1
    for i in range(4):
        if i<cnt:
            total+=row[i]
print(total)