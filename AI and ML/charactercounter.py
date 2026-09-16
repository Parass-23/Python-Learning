s=input()
s1=s.lower()
vowel=0
consonent=0
digit=0
space=0
for ch in s1:
    if ch in 'aeiou':
        vowel+=1
    elif ch>="a" and ch<="z":
        consonent+=1
    elif ch>="0" and ch<="9":
        digit+=1
    elif ch==" ":
        space+=1

       
print(vowel)
print(consonent)
print(digit)
print(space)