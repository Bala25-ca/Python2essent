menu = ["0: Add item", "1: Remove item", "2: Display list", "3: Quit"]
print("Welcome to the List Manager Menu:")
for option in menu:
    print(option)
option = int(input("Enter your option: "))
list = []
while option != 3:
    if option == 0:
        try:
            item = int(input("Enter an item to add:"))
        except ValueError:
            print("Invalid input. Please enter a valid item.")
            continue
        list.append(item)
        print("Item added to the list.", list)
    elif option == 1:
        item = input("Enter an item to remove: ")
        if item in list:
            list.pop(list.index(item))
            print("Item removed from the list.", list)
        else:
            print("Item not found in the list.", list)
    elif option == 2:
        print("Current list:", list)
    elif option == 3:
        break
    else:
        print("Invalid option. Please enter a valid option.")
        
    option = int(input("Enter your option: "))


