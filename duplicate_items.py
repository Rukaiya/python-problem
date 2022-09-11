# Display all duplicate items from a list

# using Counter container

from collections import Counter

sample_list = [10, 20, 60, 30, 20, 40, 30, 60, 70, 80]

duplicate_items = [k for k, v in Counter(sample_list).items() if v > 1]

print('Duplicate list using collection.Counter() method')
print(duplicate_items)


duplicate_items_2 = {}

for i in sample_list:
    if  i in duplicate_items_2:
        duplicate_items_2[i] += 1
    else:
        duplicate_items_2[i] = 1

result = [ k for k in duplicate_items_2.keys() if duplicate_items_2[k] > 1 ]
print('Duplicate list using loop and list comprehension')
print(result)


var= "James Bond"
print(var[2::-1])