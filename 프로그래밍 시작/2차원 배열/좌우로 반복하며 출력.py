N=int(input())
matrix=[]

for i in range(N):
    row=[]
    cnt=1
    for j in range(N):
        row.append(cnt)
        cnt+=1
    if i%2!=0:
        row.reverse()
    matrix.append(row)

for row in matrix:
    for num in row:
        print(num,end='')
    print()