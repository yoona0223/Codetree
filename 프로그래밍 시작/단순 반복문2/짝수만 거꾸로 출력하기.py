N=int(input())
N_list=input().split()
N_list.reverse()

for n in N_list:
    n=int(n)
    if n%2==0:
        print(n,end=' ')