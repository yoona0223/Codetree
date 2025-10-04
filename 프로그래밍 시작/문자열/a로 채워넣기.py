word=input()
word1=word[:1]
word2=word[1:-2]
word3=word[-2:]

word2=word2.replace(word2[0],"a",1)
word3=word3.replace(word3[0],"a",1)
print(word1+word2+word3)
