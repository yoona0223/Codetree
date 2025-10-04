N=int(input())

non=0
for i in range(N):
    n=i+1
    if n%2!=0 and n%3!=0 and n%5!=0:
        non+=1

print(non)