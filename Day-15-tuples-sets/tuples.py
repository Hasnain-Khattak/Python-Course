import timeit
import time



# print(tup2)
# print(tup)
# print(type(tup))
# print(type(tup2))
# print(tup2[0])
# tup2.append('Muhammad')
# print(tup2)

# -----------------------------------------------------------

# students = (301, 302, 303)
#
#
# print(students[0:2])


# ---------------------------------------

# empty_list = list()
# empty_dic = dict()
# empty_tuple = tuple()


# name1 = ('Ahmad', 'Muhammad')
# name2 = ('Hassan', 'Hussan', (3123, 12312))
#
# # names = ['Ahmad', 'Muhammad']
# # names.append('Hassan')
# # print(names)
#
# # for i in name1:
# #     print(i)
#
# print(name2[2][0])

# money = 1500
#
# weapens = ('smg', 'snipper', 'm24', 'm14')
# print(weapens)
#
# # weapens = list(weapens)
# # print(type(weapens))
# # weapens.append('vector')
# #
# # weapens = tuple(weapens)
# # # print(type(weapens))
# # # print(weapens)
#
# vep_name = input('Enter the name of weapen: ')
#
# if vep_name in weapens:
#     print(' It is inside you tuple')
#
# else:
#     weapens = list(weapens)
#     weapens.append(vep_name)
#     weapens = tuple(weapens)
#
# print(weapens)
# ----------------------------------------------------------------


# sets = {'Ahmad', 'Muhammad', 'Hassan', 3123, 123}
#
# sets.remove('Ahmad')
#
# print(sets)


# ------------------------------------------------------

# items = ('Ice Cream', 'Shake', 'Water')
#
# items = list(items)
# items.append('mango shake')
#
# items = tuple(items)
#
# print(items)

# ----------------------------------------------------------------------------------------

# Set of grocery items
grocery_items = {"apple", "banana", "orange"}

# Tuple of prices corresponding to the grocery items
item_prices = (1.0, 0.5, 0.75)

# Function to calculate total price
def calculate_total(item, quantity):
    if item == "apple":
        return item_prices[0] * quantity
    elif item == "banana":
        return item_prices[1] * quantity
    elif item == "orange":
        return item_prices[2] * quantity
    else:
        return 0

# Ask user input
selected_item = input("Enter the item you want to purchase (apple/banana/orange): ").lower()
quantity = int(input("Enter the quantity: "))

# Calculate total and print
total = calculate_total(selected_item, quantity)
print(f"Total price for {quantity} {selected_item}(s): ${total}")
