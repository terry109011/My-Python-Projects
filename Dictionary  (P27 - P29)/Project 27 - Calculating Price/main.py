# Project 27 - Calculating Price

import pprint

global total_price
global user_cart

total_price = 0
user_cart = {} # user_cart = {item : quantity}

available_parts = {
    1 : 'computer',
    2 : 'monitor',
    3 : 'keyboard',
    4 : 'mouse',
    5 : 'hdmi cable',
    6 : 'dvd drive',
}

price_quantity = {
    'computer' : {'price' : 500 , 'quantity' : 10},
    'monitor' : {'price' : 200 , 'quantity' : 8},
    'keyboard' : {'price' : 500 , 'quantity' : 5},
    'mouse' : {'price' : 10 , 'quantity' : 0},
    'hdmi cable' : {'price' : 20 , 'quantity' : 7},
    'dvd drive' : {'price' : 50 , 'quantity' : 5},
}

# Display items
print("Select an item.")
for keys, values in available_parts.items():
    print(f'{keys}: {values}')
print("0: To finish")
print('\n')


# Main loop
exit_app = False
while not exit_app:
    # Restraint user's input
    while True:
        try:
            option = int(input('> '))
            if option >= 0 and option < len(available_parts) + 1:
                if option != 0:
                    item = available_parts[option]
                    price = price_quantity[item]['price']
                    remaining_quantity = price_quantity[item]['quantity']
                    total_price += price
                    if remaining_quantity == 0:
                        print('Item is sold out.\n')    
                        continue
                    else:
                        # 'remaining_quantity -= 1' does not work
                        # This is the right way to update value in a nested loop
                        price_quantity[item]['quantity'] = remaining_quantity - 1    
                            
                    # Add item to user's cart
                    if item not in user_cart:
                        user_cart.setdefault(item , 1)
                    else:
                        user_cart[item] += 1
                        
                    for purchased_items, purchased_quantity in user_cart.items():
                        print(f'{purchased_items} : {purchased_quantity}')         
                    print('\n')           
                else: # if input = 0
                    print(f"Total price: ${total_price}")
                    exit_app = True
                    break
            else: # if input is out of range
                print('Please select an option from the list.')
                for keys, values in available_parts.items():
                    print(f'{keys}: {values}')
                print("0: To finish")
                print('\n')
                continue
        except ValueError or TypeError:
            print('Numeric input only. Please try again!')
            continue
