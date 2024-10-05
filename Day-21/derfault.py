# def net_price(list_price,  tax, discount=0):
#     return list_price * (1 - discount) * (1 + tax)
#
#
# print(net_price(300, 0.01))

# import time
#
#
# def count(end, start=0):
#     for x in range(start, end+1):
#         print(x)
#         time.sleep(1)
#     print('Done!')
#
#
# count(10)

# def greet(name="Student"):
#     print(f"Hello, {name}!")
#
#
# greet()          # Output: Hello, Student!
# greet("Alice")   # Output: Hello, Alice!

# def apply_discount(price, discount=10):
#     final_price = price - (price * discount / 100)
#     return final_price
#
#
# print(apply_discount(100))      # Output: 90.0
# print(apply_discount(100, 20))  # Output: 80.0


# -------------------------------------------------------------------

# *args

# def add(*args):
#     return sum(args)
#
#
# print(add(1))


# def display_name(*args):
#    print(f"Hello", end=" ")
#    for arg in args:
#        print(arg)
#
#
# names = input('Enter names: ').split(' ')
#
#
# for i in range(len(names)):
#     display_name(names[i])


# def concatenate_strings(*args):
#     return " ".join(args)
#
#
# print(concatenate_strings("Python", "is", "awesome"))  # Output: Python is awesome


#
# def demo(*args):
#     print(type(args))
#
#
# demo(12, 23, 23)
