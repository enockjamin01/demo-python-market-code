#importing operating system module
import os

class Market:

    #Category List
    category=['Fruits',
                    'Vegetables',
                            'Juice',
                                'Chips']
    
    #Dictionary of Items
    products=[
    {
        'apple':[200,30],
        'banana':[300,40],
        'orange':[400,20],
        'blueberries':[300,50]
    },

    {
        'okra':[300,10],
        'tomato':[400,10],
        'springonions':[500,30],
        'onions':[300,20]
    },

    {
        'coke':[200,20],
        'pepsi':[400,20],
        'mountaindew':[500,20],
        'sting':[300,20]
    },

    {
        'lays':[300,10],
        'bingo':[400,10],
        'doritos':[300,10],
        'pringles':[200,90]
    }]

    """It is a static method that accepts two arguments
        1. The List of category
        2. The List of products
        it accepts the two arguments and arranges the product table"""
    @staticmethod
    def existing_table(category,products):
        for index in range(0,len(category)):
            print(category[index])
            print('-------------------------------------------------------------')
            for k,v in products[index].items():
                print('Products: ',k.upper(),' Quantity: ',v[0],' Price: ',v[1])
            print('-------------------------------------------------------------')
            print()
    
    """It is a method used to request user about
        1.Category of item
        2.Item
        3.Quantity of item
        and reteuns those value"""
    def user_cart(self):
        category=str(input('Enter the product category: '))
        product=str(input('Enter the product: '))
        if category.lower() == 'juice':
            quantity=int(input('Enter the number of bottles: '))
        elif category.lower() == 'chips':
            quantity=int(input('Enter the number of packets: '))
        elif category.lower() == 'fruits' or  category.lower() == 'vegetables':
            quantity=int(input('Enter the number of KG: '))
        else:
            quantity=0
            category='Error'
            product='Error'
            print('Invalid inputs please try again....')

        print()
        
        
        return category,product,quantity

    """It is a static method which accepts 4 argument
        1.The Prodcut list  2. Category 3.Product 4. Quantity
        and it returms the amount of user bill"""
    @staticmethod
    def amount_calculator(product_lst,category,product,quantity):
            if 'fruits' == category:
                fruit_per_kg=int(product_lst[0][product][1])
                amount=fruit_per_kg*quantity
            
            elif 'vegetables' == category:
                vegetables_per_kg=int(product_lst[1][product][1])
                amount=vegetables_per_kg*quantity

            elif 'juice' == category:
                juice_per_bottle=int(product_lst[2][product][1])
                amount=juice_per_bottle*quantity

            elif 'chips' == category:
                chips_per_packet=int(product_lst[3][product][1])
                amount=chips_per_packet*quantity
            
            return amount
    
    """It is used to display user bill by taking 4 arguments
        1.category 2.product 3.quantity 4.amount"""
    def user_bill(self,category,product,quantity,amount):
        print('Your Bill')
        print('Category:',category.upper())
        print('Product:',product.upper())
        if category.lower() == 'juice':
            print('Quantity:',quantity,'bottles')
        elif category.lower() == 'chips':
            print('Quantity:',quantity,'packets')
        elif category.lower() == 'fruits' or  category.lower() == 'vegetables':
            print('Quantity:',quantity,'Kg')
        else:
            print('Quantity Ivalid: ',quantity)
        print('Amount: ',amount)
        print()
    
    """Its a staticmethod used to give the updated product table after billing
        it takes 5 arguments
        1.product list  2.category list 3.category 4.product 5.quantity"""
    @staticmethod
    def updated_table(product_lst,category_lst,category,product,quantity):
        if 'fruits' == category:
            product_lst[0][product.lower()][0]-=quantity
        
        elif 'vegetables' == category:
            product_lst[1][product.lower()][0]-=quantity
        
        elif 'juice' == category:
            product_lst[2][product.lower()][0]-=quantity

        elif 'chips' == category:
            product_lst[3][product.lower()][0]-=quantity
        
        for index in range(0,len(category_lst)):
            print(category_lst[index])
            print('-------------------------------------------------------------')
            for k,v in product_lst[index].items():
                print('Products: ',k.upper(),' Quantity: ',v[0],' Price: ',v[1])
            print('-------------------------------------------------------------')
            print()
    
#Class used to generate user bill as text file
class BillGenerator():

    """This is a static method used to create a text file
        taking 6 arguments 1.phone_number 2.username 3.category 4.product 5.quantity 6.amount"""
    @staticmethod
    def generate_bill(phone_number,username,category,product,quantity,amount):
        extension='.txt'
        file_name=phone_number+extension
        if os.path.isfile(file_name):
            coloum_lst=['Category: ','Product: ','Quantity: ','Amount: ']
            detail_lst=[str(category),str(product),str(quantity),str(amount)]
            file=open(file_name,'a+')
            file.write('\n')
            for detail_index in range(0,len(coloum_lst)):
                file.write(coloum_lst[detail_index]+detail_lst[detail_index]+'\n')
            file.close()
            print('Bill Generated Successfully')
            print()

        else:
            file=open(file_name,'w')
            coloum_lst=['Phone Number: ','Name: ','Category: ','Product: ','Quantity: ','Amount: ']
            detail_lst=[str(phone_number),str(username),str(category),str(product),str(quantity),str(amount)]
            for detail_index in range(0,len(coloum_lst)):
                file.write(coloum_lst[detail_index]+detail_lst[detail_index]+'\n')
            file.close()
            print('Bill Generated Successfully')
            print()


#Users Managment
i=0
flag=None
number_of_users=1

for user in range(0,100):
    user=Market()
    phone_number=input('Enter your phonenumber: ')
    username=input('Enter your name: ')
    Market.existing_table(user.category,user.products)
    category,product,quantity=user.user_cart()
    amount=Market.amount_calculator(user.products,category,product,quantity)
    user.user_bill(category,product,quantity,amount)
    Market.updated_table(user.products,user.category,category,product,quantity)
    BillGenerator.generate_bill(phone_number,username,category,product,quantity,amount)
    number_of_users+=1
    flag=str(input('Do you want to continue (y/n): '))
    if flag == 'y':
        print()
        print("Next User")
        continue
    elif flag.lower() == 'n':
        print()
        print("Closed")
        break
    else:
        print()
        print('Invalid Entry')
        break