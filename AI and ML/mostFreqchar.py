string=input()
word={}
for ch in string:
  if ch!=" ":
    if ch not in word:
        word[ch]=1
    else:
        word[ch]+=1
maxv=0
for k,v in word.items():
   
   if v>maxv:
    maxv=v
    maxkey=k
print(maxkey)



    
