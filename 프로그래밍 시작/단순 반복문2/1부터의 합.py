N=int(input())

n=0
for i in range(1,5000):
    n=n+i
    if n>=N:
        print(i)
        break