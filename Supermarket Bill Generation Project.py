#Supermarket Bill Generation Project
from _datetime import datetime
name = input('Enter your name: ')
#LIST of item
lists = '''
Rice    RS 20/Kg
Sugar   Rs 30/Kg
salt    Rs 20/Kg
Oil     Rs 80/Kg
Paneer  Rs 110/Kg
Maggi   Rs 50/Kg
Boost   Rs 90/Kg
Clogate Rs 85/each '''
price = 0
pricelist = []
totalprice = 0
finalprice = 0
ilist = []
qlist = []
plist = []
#rates for items
items ={'rice':20,'sugar':30,'salt':20,'oil':80,'paneer':110,'maggi':50,'boost':90,'clogate':85}
option=int(input("For list of items press 1: "))
if option==1:
    print(lists)
for i in range(len(items)):
    inp1=int(input('If you want to buy press 1 or 2 for exit: '))
    if inp1==2:
        break
    if inp1==1:
        item=input("Enter your items: ")
        quantity = int(input("Enter the Quantity: "))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            GST=(totalprice*5)/100
            finalamount=GST+totalprice
        else:
            print('Sorry,you entered wrong number')
    inp=input('Can bill the items yes or no:')
    if inp=='yes':
        pass
        if finalamount!=0:
            print(25*'=','Jagadeesh Supermarket',25*'=')
            print(28*' ','TIRUPATI')
            print('Name:',name,30*' ','Date:',datetime.now())
            print(75*'-')
            print('sno:',8*' ','items:',8*' ','Quantity',3*' ','price')
            for i in range(len(pricelist)):
                print(i,8*' ',2*' ',ilist[i],13*' ',qlist[i],8*' ',plist[i])
                print(75*'-')
                print(50*' ','Total Amount:','Rs',totalprice)
                print('GST Amount',50*' ','   Rs',GST)
                print(75*'-')
                print(50*' ','Final Amount:','Rs',finalamount)
                print(50*' ', 'Thanks for Visiting')
                print(75 * '-')

