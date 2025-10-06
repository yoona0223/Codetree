fruits=["apple","banana","grape","blueberry","orange"]
letter=input()
cnt=0
for fruit in fruits:
    if fruit[2]==letter or fruit[3]==letter:
        print(fruit)
        cnt+=1
print(cnt)