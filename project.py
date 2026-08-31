#varibles
#A person wants to calculate their monthly income, expenses, savings, yearly savings, and savings percentage.

print("===== PERSONAL FINANCE REPORT =====")

#information of the empolyee

a=input("enter the name of empolyee:")
b=int(input("enter the age of empolyee:"))
c=input("enter the city name of person:")


#calculate montly income
salary=int(input("\nenter the salry of the person:"))
freenclacing=int(input("enter the freelacing earning:"))
otherincome=int(input("enter the other income of the empolyee:"))

montly_income=salary+freenclacing+otherincome


#montly expences
rent=int(input("\nrent :"))
electricity_bill=int(input("enter the electricity bill:"))
gas_bill=int(input("enter the gas bill:"))
transport=int(input("enter the transport bill:"))
houseitembill=int(input("grocery bill:"))
iternet=int(input("internet bill:"))
shopping_bill=int(input("enter the shopping bill:"))
other_bill=int(input("extra money spending:"))

montly_expences=rent+electricity_bill+gas_bill+transport+houseitembill+iternet+shopping_bill+other_bill


#montly saving
montly_saving=montly_income-montly_expences


#calculate yearly income
yearly_income=montly_income*12



#calculate yearly expences
yearly_expences=yearly_income*12


#calculate yearly saving
yearly_saving=montly_saving*12



#saving percentage
saving_percentage=yearly_saving*100/yearly_income


#average daily expences
daily_expences=montly_expences/30



#print all things
print("\n===== PERSONAL FINANCE REPORT =====")
print(f'NAME :{a}')
print(f'Age:{b}')
print(f'city:{c}')


print(f'\nthe montly income :{montly_income}')
print(f'the montly expences:{montly_expences}')
print(f'the montly  saving:{montly_saving}')


print(f'\nyearly income:{yearly_income}')
print(f'yearly expences:{yearly_expences}')
print(f'yearly saving:{yearly_saving}')

print(f'\nsaving percentage:{saving_percentage}')
print(f'daily expences:{daily_expences}')



#project 2: E-Commerce Sales & Profit Analyzer 

#product informations
products = {
    "product1": {
        "name": "Laptop",
        "category": "Electronics",
        "price": 50000,
        "quantity": 20,
        "discount": 10
    },

    "product2": {
        "name": "Smartphone",
        "category": "Electronics",
        "price": 25000,
        "quantity": 30,
        "discount": 5
    },

    "product3": {
        "name": "Headphones",
        "category": "Accessories",
        "price": 3000,
        "quantity": 50,
        "discount": 8
    },

    "product4": {
        "name": "Keyboard",
        "category": "Accessories",
        "price": 2000,
        "quantity": 40,
        "discount": 5
    }
}



#CALCULATE 1ST PRODUCTS
#step1:print e-commerce sales analysis
print("========================================")
print("    E-COMMERCE SALES ANALYSIS")
print("========================================")

#step 2:print the 1st product details
r="product1"

for product, details in products.items():
    for key,value in details.items():
        if product==r:
            print(key,":",value)


#step 3 calculate revenue for 1st products

a = products["product1"]["price"]

b = products["product1"]["quantity"]
d=products["product1"]["discount"]
c = a * b
e=int(c*d/100)
print("\nRevenue:", c)
print("Discount Amount:",e)
f=c-e
print("Final Sales Amount:",f)


#step 4:print ---------------------------------------

print("\n---------------------------------------")


#step 5:print 2 products
r="product2"

for product, details in products.items():
    for key,value in details.items():
        if product==r:
            print(key,":",value)


#step 6: calculate revenue for 2nd products

a = products["product2"]["price"]

b = products["product2"]["quantity"]
d=products["product2"]["discount"]
c1 = a * b
e1=int(c*d/100)
print("\nRevenue:", c1)
print("Discount Amount:",e1)
f1=c-e
print("Final Sales Amount:",f1)


#step 7:print ---------------------------------------

print("\n---------------------------------------")

#step 8:print 3 products
r="product3"

for product, details in products.items():
    for key,value in details.items():
        if product==r:
            print(key,":",value)


#step 9: calculate revenue for 3rd products

a = products["product3"]["price"]

b = products["product3"]["quantity"]
d=products["product3"]["discount"]
c2 = a * b
e2=int(c*d/100)
print("\nRevenue:", c2)
print("Discount Amount:",e2)
f2=c-e
print("Final Sales Amount:",f2)


#step 10:print ---------------------------------------

print("\n---------------------------------------")

#step 11:print 4 products
r="product4"

for product, details in products.items():
    for key,value in details.items():
        if product==r:
            print(key,":",value)


#step 12:calculate revenue for 4 products

a = products["product4"]["price"]

b = products["product4"]["quantity"]
d=products["product4"]["discount"]
c3 = a * b
e3=int(c*d/100)
print("\nRevenue:", c3)
print("Discount Amount:",e3)
f3=c-e
print("Final Sales Amount:",f3)



#step 13:print
print("\n========================================")
print("         TOTAL SALES SUMMARY")
print("========================================")

#step 14:calculate total revenue of all products 
total_revenue=c+c1+c2+c3
total_discount=e+e1+e2+e3
final_sales_amount=total_revenue-total_discount
print("\nTotal Revenue:",total_revenue)
print("Total Discount:",total_discount)
print("Final Sales Amount:",final_sales_amount)

#step 15:print
print("\n========================================")



"2nd technique to used for easy this project"
products = {
    "product1": {
        "name": "Laptop",
        "category": "Electronics",
        "price": 50000,
        "quantity": 20,
        "discount": 10
    },

    "product2": {
        "name": "Smartphone",
        "category": "Electronics",
        "price": 25000,
        "quantity": 30,
        "discount": 5
    },

    "product3": {
        "name": "Headphones",
        "category": "Accessories",
        "price": 3000,
        "quantity": 50,
        "discount": 8
    },

    "product4": {
        "name": "Keyboard",
        "category": "Accessories",
        "price": 2000,
        "quantity": 40,
        "discount": 5
    }
}
print("========================================")
print("    E-COMMERCE SALES ANALYSIS")
print("========================================")

total_revenue=0
total_discount=0

for product,details in products.items():
    revenue=details["price"]*details["quantity"]
    discount=(revenue*details['discount'])/100
    sales=revenue-discount

    total_revenue=total_revenue+revenue
    total_discount=total_discount+discount
    final_sales_amount=total_revenue-total_discount

    print('\nproduct name:',details['name'])
    print("categroy:",details["category"])
    print("price:",details["price"])
    print("quantinty:",details["quantity"])
    print("discount:",details["discount"])
    print("\nrevenue:",revenue)
    print("dicount amount:",discount)
    print("Final Sales Amount:",sales)

    print("\n----------------------------------------")
    print("\n========================================")
print("         TOTAL SALES SUMMARY")
print("========================================")

print("Total Revenue:", total_revenue)
print("Total Discount:", total_discount)
print("Final Sales Amount:", final_sales_amount)

