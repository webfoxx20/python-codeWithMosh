import math

lists = ["bots",4,False, {"id":1, "name":"ted lanzo"}]
print(lists)

# combining two list together
lists2 = [2] *3
print(lists + lists2)

# create a list with iterable
list3 = list(range(1,11))
print(len(list3))

# Accessing an element in a list
print(lists[0])

# updating a list
lists[0] = "machine"
print(lists)
print(lists[len(lists) -1])

# get specific part of the list
print(lists[0:2])

# skipping an element in the list

print(lists[0::3])
numbers = list(range(1,11))

print(numbers[::4])

# unpacking a list
first , second , third , *other_number = numbers
print(first)
print(second)
print(other_number)

# packed *other_number

# get the last number
item1 , *other_item ,  last_item  = numbers
print(last_item)

# iterating  a list
for index , number in enumerate(numbers):
    print( f"index is {index} :::::: value is {number}")

# adding item in a list
# add an item  after the last item
numbers.append(12)
print(numbers)
# insert  item in a specific index
numbers.insert(5,"bots")
print(numbers)


# Removal of item in a list
# remove last item in a string
numbers.pop()
print(numbers)
# remove item from a specific position
numbers.pop(4)
print(numbers)

# delete more than one item in the list
del numbers[0:4]
print(numbers)

# delete all the record in the list
numbers.clear()
print(numbers)

# get the index of the item
item_index = list(range(1,5))

print(item_index.index(3))

# get the count of an item in a list
if item_index.count(6) == 0:
     print("number 6 doesn't exist in the list.")

products = [  ("product2", 30), ("product1", 20) ,("product5", 25), ("product3", 40) ,("product4", 10)   ]



products.sort(key = lambda item:item[1])
print(products)

# map
# get the price of the
prices = list(map(lambda item:item[1],products))
product_item = list(map(lambda item:item[0],products))

print(prices)
print(product_item)


# filter
filtered_price = list(filter(lambda price:price[1] >20, products))
print(filtered_price)


# list comprehension
map_expression =  [product[1] for product in products]
print(map_expression)

# filter comprehension
filter_comprehension = [product  for product in products if product[1] > 20 ]
print(filter_comprehension)

# zippina two to a tuple.
list1 = [1,2,3]
list2 = [4,5,6]

print(list(zip(list1,list2)))


