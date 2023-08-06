print("Welcome to the burger shop, please enter the size you want:\nLarge: L\nNormal: N\nMini: M")
size = input("Enter size (L, N, M): ")
add_mushroom = input("Add mushroom? Y or N: ")
extra_cheese = input("Extra cheese? Y or N: ")

if size == "L" or size == "l":
    cost = 10
elif size == "N" or size == "n":
    cost = 8
elif size == "M" or size == "m":
    cost = 5
        
if add_mushroom == "Y" or add_mushroom == "y":
    if size == "L" or size == "l":
        cost += 2
    else:
        cost += 1
        
if extra_cheese == "Y" or extra_cheese == "y":
    cost += 1        
        
print(f'Your final bill is: {cost}.')