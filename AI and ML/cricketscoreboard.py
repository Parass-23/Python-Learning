scores={

}
for i in range(3):
    p=input()
    r=int(input())
    scores[p]=r

maxscore=0
totalscore=0
for score in scores:
    if scores[score]>maxscore:
        maxscore=scores[score]
        maxscorer=score
    totalscore+=scores[score]

print(maxscore,maxscorer)
print(totalscore//len(scores))



