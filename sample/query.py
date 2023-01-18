"""Command line interface to query the stock.

To iterate the source data you can use the following structure:

for item in warehouse1:
    # Your instructions here.
    # The `item` name will contain each of the strings (item names) in the list.
"""

from data import stock

# YOUR CODE STARTS HERE

# Get the user name

# Greet the user

# Show the menu and ask to pick a choice

# If they pick 1
#
# Else, if they pick 2
#
# Else, if they pick 3
#
# Else

# Thank the user for the visit

item_counter_warehouse_one = 0
item_counter_warehouse_two = 0


user_name = input("Hello! What is you name: ")
print(f"Hello, {user_name}")

print("(1) List items by warehouse (2) Search an item an place an order (3) Quit")

choice = int(input("Which option do you choose: "))

if choice == 1:
    
    ### Printing all items of Warehouse 1
    print("+" * 100)
    print("WAREHOUSE 1")
    print("+" * 100)

    for item in stock:
        if item['warehouse'] == 1:
            print(item['category'])
    
    ### Printing all items of Warehouse 2
    print("+" * 100)
    print("WAREHOUSE 2")
    print("+" * 100)

    for item in stock:
        if item['warehouse'] == 2:
            print(item["category"])

elif choice == 2:

    ### Ask user to input an item
    item_user_choice = input("What item do you wanna search for: ")

    ### Print total amount of that chosen item in each Warehouse
    for item in stock:
        if item['warehouse'] == 1 and item["category"] == item_user_choice: 
            item_counter_warehouse_one += 1
        if item['warehouse'] == 2 and item["category"] == item_user_choice:
            item_counter_warehouse_two += 1

    if item_counter_warehouse_one > 0 and item_counter_warehouse_two == 0:
        print(f"Item can only be found in Warehouse 1. The amount is {item_counter_warehouse_one}")
    elif item_counter_warehouse_two > 0 and item_counter_warehouse_one == 0:
        print(f"Item can only be found in Warehouse 2. The amount is {item_counter_warehouse_two}")
    elif item_counter_warehouse_one > 0 and item_counter_warehouse_two > 0:
        print(f"Item can be found in both Warehouses. The amount is {item_counter_warehouse_one + item_counter_warehouse_two}")
        if item_counter_warehouse_one > item_counter_warehouse_two:
            print(f"Amount of item is highest in Warehouse 1. It's there {item_counter_warehouse_one} time(s).")
        else:
            print(f"Amount of item is highest in Warehouse 2. It's there {item_counter_warehouse_two} time(s).")

    else:
        print("Not in stock.")

    ### Ask user if they want to place an order on that item
    item_user_order = input("Do you wanna place an order on that item (y/n): ")

    if item_user_order == "y":
    
    ### Ask user for amount of items
        item_user_order_amount = int(input("How many times do you wanna order this item: "))

    ### Checking for availability and place order eventually
        if item_user_order_amount <= item_counter_warehouse_one + item_counter_warehouse_two:
            print(f"The order has been placed. You ordered {item_user_choice} {item_user_order_amount} time(s).")
        elif item_user_order_amount > item_counter_warehouse_one + item_counter_warehouse_two:
            print("You exceeded the maximum availability.")
            item_user_order_amount_max = input("Do you wanna order the maximum available instead (y/n): ")
            if item_user_order_amount_max == "y":
                print(f"The order has been placed, You ordered {item_user_choice} {item_counter_warehouse_one + item_counter_warehouse_two} time(s).")
            elif item_user_order_amount_max == "n":
                print(f"Never mind {user_name}. See you next time!")
            else:
                print(f"Input is not accepted. Please start again.")

    elif item_user_order == "n":
        print(f"Thank you {user_name}! See you next time")
    else:
        print(f"Input is not accepted. Please start again.")

elif choice == 3:
    pass
