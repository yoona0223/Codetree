word=input().split()
word1=len(word[0])
word2=len(word[1])
if word1>word2:
    print(word[0],word1)
elif word1<word2:
    print(word[1],word2)
else:
    print("same")