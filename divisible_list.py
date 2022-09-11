# Display numbers divisible by 5 from a list
l =  [10, 20, 33, 46, 55]
result = [x for x in l if x % 5 == 0]

print("input list: ", l)
print("List Divisible by 5 is: ", result)