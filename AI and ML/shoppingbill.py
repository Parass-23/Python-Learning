item=[]
prices=[]
for i in range(3):
    name=input()
    price=int(input())

    item.append(name)
    prices.append(price)

totalbill=sum(prices)
mx=0
mx_prd=" "
mn=0
mn_prd=" "
for i in range(3):
    if prices[i]>mx:
        mx_prd=item[i]
        mx=prices[i]
    elif prices[i]<mn:
        mn_prd=item[i]
        mn=prices[i]
print(totalbill)
print(mx,mx_prd)
print(mn,mn_prd)

