#-------------------------VEGETABLE SHOP---------------------------------
from datetime import datetime
veg = ['brinjal','potato','carrot','cucumber','tomato','onion','chilli']
quantity = [10.0,15.0,20.0,30.0,45.0,35.0,50.0]
sellingPrice = [30,40,35,30,25,20,20]
costPrice = [15,20,17,15,12,10,10]
cust_name = ['sateesh','raju','pranavi','vcube']  
cust_contact = [9845723865,7016345379,9492652345,1234567890]
revenue = 0
profit = 0
revItem = []
revProfit = []
revSP = []
cust_amt = [400,250,300,150]
while True:
    cart_item = []
    cart_qty = []
    cart_sp = []
    vegProfit = []
    amt = 0
    print('-'*20,'HOME PAGE','-'*19)
    print('1.Customer')
    print('2.Shopkeeper')
    print('3.Exit')
    user = input('Enter your choice(1/2/3): ')
    if user == '1':  #Customer
        while True:
            cust = input('Enter your name: ')
            if not cust.isdigit():
                while True:
                    num = input('Enter your mobile number: ')
                    if not num.isdigit():
                        print('Enter valid input')
                        continue
                    else:
                        if len(num) != 10:
                            print('Error:Maximum limit exceeded')
                            continue
                        else:
                            x = int(num)
                            if x in cust_contact and cust not in cust_name:
                                print('Number already exists with a different user')
                                continue
                            elif cust in cust_name and x in cust_contact:
                                print('>>>Thank you for being our loyal customer<<<')
                                break
                            elif x not in cust_contact and cust not in cust_name:
                                print('Proceeding to shop.....')
                                cust_name.append(cust)
                                cust_contact.append(x)
                                break
                            else:
                                pass
            else:
                print('Invalid input!')
                continue
            break
        #------------
        print('*'*12,'Welcome to Vegetable Shop','*'*11)
        while True:
            print('-'*50)
            print('1.Add items to cart')
            print('2.Remove item from cart')
            print('3.Modify the cart')
            print('4.View cart')
            print('5.Go for billing')
            print('6.Exit')
            ch = (input('Enter your choice(1/2/3/4/5/6): '))
            print('-'*50)
            if ch == '1':  #add to cart
                print('Items      Price      Qty(in kg)')
                for k,v,n in zip(veg,sellingPrice,quantity):
                    print(k,'   ',v,'    ',n)
                print('-'*50)
                while True:
                    item = input('What is the vegetable you want: ').lower()
                    if not item.isdigit():
                        if item in veg:
                            if item not in cart_item:
                                while True:
                                    qty = input('Quantity(in kilograms): ')
                                    if qty.isdigit():
                                        qty = float(qty)
                                        idx = veg.index(item)
                                        if qty <= quantity[idx]:
                                            cart_item.append(item)  #item
                                            cart_qty.append(qty)    #qty
                                            print('Added item to cart')
                                            print('-'*50)
                                            sp = qty*sellingPrice[idx]
                                            cart_sp.append(sp)      #price
                                            amt = amt + sp
                                            cp = qty*costPrice[idx]
                                            itemProfit = sp-cp
                                            vegProfit.append(itemProfit)   #profit
                                            quantity[idx] = quantity[idx] - qty   #qty update
                                            break
                                        else:
                                            print('Insufficient stock!')
                                            continue
                                    else:
                                        print('Invalid input!')
                            else:
                                print('Already exists!')
                        else:
                            print('Unavailable in stock!')
                    else:
                        print('Invalid input!')
                    l = input('Do you want to add one more vegetable(yes/no): ').lower()
                    if l=='no':
                        break
                    elif l=='yes':
                        continue
                    else:
                        print('invalid input')
                        
            elif ch == '2': #remove from cart
                item = input('Enter the vegetable name: ').lower()
                if not item.isdigit():
                    if item in cart_item:
                        idx = veg.index(item)
                        idx1 = cart_item.index(item)
                        cart_item.remove(item)
                        qtyRemoved = cart_qty.pop(idx1)
                        quantity[idx] = quantity[idx] + qtyRemoved
                        spRemoved = cart_sp.pop(idx1)
                        amt = amt - spRemoved                        
                        vegProfit.pop(idx1)                        
                        print(f'{item}: Removed from cart!')
                    else:
                        print('Item does not exist in cart!')
                else:
                    print('Invalid input!')
            elif ch == '3':  #modify cart
                item = input('Enter the vegetable name: ').lower()
                if not item.isdigit():
                    if item in cart_item:
                        idx = veg.index(item)
                        idx1 = cart_item.index(item)
                        print('1.Increase quantity')
                        print('2.Reduce quantity')
                        a = input('Enter your choice(1/2): ')
                        if a == '1': #increase
                            while True:
                                q = input('Enter the quantity to be added: ')
                                if q.isdigit():
                                    q = float(q)
                                    if q <= quantity[idx]:
                                        cart_qty[idx1] = cart_qty[idx1] + q
                                        sp = q*sellingPrice[idx]
                                        cart_sp[idx1] = cart_sp[idx1] + sp 
                                        amt = amt + sp
                                        cp = q*costPrice[idx]
                                        itemProfit = sp-cp
                                        vegProfit[idx1]= vegProfit[idx1]+itemProfit 
                                        quantity[idx] = quantity[idx] - q
                                        print('Successfully modified cart!')
                                        break
                                    else:
                                        print('Insufficient stock!')
                                        continue
                                else:
                                    print('Invalid input!')
                        elif a == '2': #reduce
                            while True:
                                q = input('Enter the quantity to be reduced: ')
                                if q.isdigit():
                                    q = float(q)
                                    if q <= cart_qty[idx1]:
                                        cart_qty[idx1] = cart_qty[idx1] - q
                                        cart_sp[idx1] = cart_qty[idx1]*sellingPrice[idx]
                                        sp = q*sellingPrice[idx]
                                        amt = amt - sp
                                        cp = cart_qty[idx1]*costPrice[idx]
                                        vegProfit[idx1] = cart_sp[idx1]-cp
                                        quantity[idx] = quantity[idx] + q
                                        print('Successfully modified cart!')
                                        break
                                    else:
                                        print('Insufficient stock in cart!')
                                        continue
                                else:
                                    print('Invalid input!')
                        else:
                            print('Invalid input!')                        
                    else:
                        print('Item does not exist in cart!')
                else:
                    print('Invalid input!')
            elif ch == '4':  #view cart
                print('-'*24,'CART','-'*20)
                print('Item      Qty      Price')
                for k,v,n in zip(cart_item,cart_qty,cart_sp):
                    print(k,'   ',v,'   ',n)
            elif ch == '5':  #Billing               
                print('*'*18,'PURCHASE BILL','*'*17)
                print('Customer name:',cust)
                print('Mobile number:',num)
                current_datetime = datetime.now()
                purchase_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
                print("Purchase Date and Time:", purchase_datetime)
                print('-'*50)
                print('Item      Qty       Price')
                for k,v,n in zip(cart_item,cart_qty,cart_sp):
                    print(k,'   ',v,'   ',n)
                print('Total items:',len(cart_item))
                s = 0
                for i in cart_qty:
                    s = s + i                    
                for i in range(0, len(cart_item)):
                    item = cart_item[i]
                    if item not in revItem:
                        revItem.append(item)
                        revProfit.append(vegProfit[i])  
                        revSP.append(cart_sp[i]) 
                    else:
                        idx = revItem.index(item)
                        revProfit[idx] += vegProfit[i]  
                        revSP[idx] += cart_sp[i]
                print('Total quantity:',s)
                print('Total purchase price:',amt)
                cust_amt.append(amt)
                break    
            elif ch=='6':
                print('Exiting....')
                break
            else:
                print('Choose correct option!')
        print()
        print('*'*15,'Thanks for visiting','*'*14)
        pro = 0
        for i in vegProfit:
            pro = pro+i
        revenue = revenue + amt  
        profit = profit + pro
#----------------------------------------------------------------------------------------
    elif user == '2':  #Shopkeeper
        while True:
            name = input('Username: ')
            code = input('Password: ')
            if name != 'vcube' and code != 'vcube@123':
                print('Invalid credentials!')
            elif name != 'vcube':
                print('Invalid username!')
            elif code != 'vcube@123':
                print('Invalid password!')
            else:
                print('Access granted!')
                break
        while True:
            print('-'*20,'MAIN MENU','-'*19)
            print('1.Add vegetable')
            print('2.Remove vegetable')
            print('3.Modify quantities')
            print('4.View Remaining Stock Report')
            print('5.View customer details')
            print('6.Itemized revenue and profit')
            print('7.Total revenue and profit for the day')
            print('8.Exit')
            choice = input('Enter your choice(1/2/3/4/5/6/7/8): ')
            print('-'*50)
            if choice == '1':#add
                addVeg = input('Enter the name of the vegetable: ').lower()
                if not addVeg.isdigit():
                    if addVeg not in veg:
                        while True:
                            qty = input('Enter the quantity(in kilograms): ')
                            if qty.isdigit():
                                qty = float(qty)
                                sp = int(input('Enter the selling price: '))
                                cp = float(input('Enter the cost price: '))
                                veg.append(addVeg)
                                quantity.append(qty)
                                sellingPrice.append(sp)
                                costPrice.append(cp)
                                print('Successfully added the Vegetable!')
                                break
                            else:
                                print('Invalid input!')
                    else:
                        print('Already exists!')
                else:
                    print('Invalid input!')
            elif choice == '2':#remove
                removeVeg = input('Enter the name of the vegetable: ').lower()
                if not removeVeg.isdigit():
                    if removeVeg in veg:                        
                        idx = veg.index(removeVeg)                        
                        veg.remove(removeVeg)
                        quantity.pop(idx)
                        sellingPrice.pop(idx)
                        costPrice.pop(idx)
                        print('Successfully removed!')
                    else:
                        print('Not available in stock!')
                else:
                    print('Invalid input!')                    
            elif choice == '3': #modify
                modifyVeg = input('Enter the name of the vegetable: ').lower()
                if not modifyVeg.isdigit():
                    if modifyVeg in veg:
                        print('1.Price')
                        print('2.Quantity')
                        ch = input('Enter your choice(1/2): ')
                        idx = veg.index(modifyVeg)
                        if ch == '1': #price
                            sp = input('Enter the updated selling price: ')
                            cp = input('Enter the updated cost price: ')
                            sellingPrice[idx] = float(sp)
                            costPrice[idx] = float(cp)
                            print('Successfully modified!')
                        elif ch == '2': #qty
                            print('1.Increase quantity')
                            print('2.Decrease quantity')                           
                            s = input('Enter your choice(1/2): ')
                            if s == '1': #add qty
                                while True:
                                    newQty = float(input('Enter the quantity to be increased: '))
                                    if newQty.isdigit():
                                        quantity[idx] = quantity[idx] + newQty
                                        print('Successfully modified!')
                                        break
                                    else:
                                        print('Invalid input!')
                            elif s == '2': #sub qty
                                while True:
                                    newQty = float(input('Enter the quantity to be reduced: '))
                                    if newQty.isdigit():
                                        if newQty <= quantity[idx]:
                                            quantity[idx] = quantity[idx] - newQty
                                            print('Successfully modified!')
                                            break
                                        else:
                                            print('Error: Insufficient stock!')
                                            continue
                                    else:
                                        print('Invalid input!')                            
                            else:
                                print('Choose correct option!')                           
                        else:
                            print('Choose correct option!')
                    else:
                        print('Not available in stock')
                else:
                    print('Invalid input!')                       
            elif choice == '4':  #available stock
                print('*'*16,'AVAILABLE STOCK','*'*17)
                print('Item      Qty      Cost')
                for k,v,u in zip(veg,quantity,sellingPrice):
                    print(k,'   ',v,'   ', u)
            elif choice == '5': #customer details
                print('*'*16,'CUSTOMER DETAILS','*'*16)
                print('Customer name   Contact number    Revenue')
                for k,v,n in zip(cust_name,cust_contact,cust_amt):
                    print(k,'        ',v,'        ',n)
            elif choice == '6':  #item revenue and profit
                print('*'*17,'REVENUE REPORT','*'*17)
                print('Item      Profit       Revenue')
                for k,v,n in zip(revItem,revProfit,revSP):
                    print(k,'   ',v,'   ',n)
                print()
                rev = 0
                pro = 0
                for i in revSP:
                    rev = rev+i
                for i in revProfit:
                    pro = pro+i
                print('-'*50)
                print('Total revenue:',rev)
                print('Total profit:',pro)
                print('-'*50)               
            elif choice == '7':  #Total profit and revenue
                print('Total Revenue for the day: ',revenue)
                print('Total profit for the day: ',profit)
            elif choice == '8': #exit
                print('Logged out successfully!')
                break
            else:
                print('Choose correct option!')
        ch = input('Do you want to close the shop(yes/no): ')
        if ch == 'yes':            
            print('-'*17,'Remaining stock','-'*16)
            for k,v in zip(veg,quantity):
                print(k,'   ',v)
            print('-'*50)
            print('Total Revenue for the day: ',revenue)
            print('Total profit for the day: ',profit)
            print('>'*18,'SHOP CLOSED','<'*19)
            break
    elif user == '3':
        print('Exiting the application....')
        break
    else:
        print('Choose correct option!')
               

