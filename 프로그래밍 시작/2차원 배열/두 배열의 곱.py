matrix1=[list(map(int,input().split())) for _ in range(3)]
input()
matrix2=[list(map(int,input().split())) for _ in range(3)]

new_matrix=[
    [matrix1[r][c]*matrix2[r][c] for c in range(3)]
    for r in range(3)
]

for row in new_matrix:
    for element in row:
        print(element,end=' ')
    print()