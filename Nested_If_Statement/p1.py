'''
7. Consider a restaurant which sells 3 different pizza ('Cheese Loaded','Veg Loaded','Non Veg Loaded')\
    at the price of 120,180,240 respectively. Customer can order 1 variety of pizza at a time and can order\
    'n' no. of pizza in the same flavour. If any add-ons is required customer can opt 1 add-on along with the\
    order. Available add-ons are ('Extra Cheese','Extra Ketchup') at the price of 20 each. Based on the \
    customer's order calculate the total bill using nested if statements.
'''
pizza_menu = {'Cheese Loaded':120,'Veg Loaded':180,'Non Veg Loaded':240}
add_ons = {"Extra Cheese":20,"Extra Ketchup":20}
bill = 0
order = input("Which Pizza do you want? \n")
qty = int(input("Enter quantity: \n"))
extra_add_on = input("Do you need add-ons? y/n: ")
if order in pizza_menu:
    bill = pizza_menu[order] * qty
    if extra_add_on == 'Y' or extra_add_on == 'y':
        which_add_on = input('Which add-on you want? \n')
        if which_add_on in add_ons:
            bill += add_ons[which_add_on]
print(bill)
