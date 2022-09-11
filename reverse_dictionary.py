# Reverse Dictionary mapping
ascii_dict = {'A': 65, 'B': 66, 'C': 67, 'D': 68}

# using dictionary comprehension
new_dict = { value: key for key, value in ascii_dict.items()}
print(new_dict)


reverse_dict = {}
for k, v in ascii_dict.items():
    reverse_dict[v] = k

print(reverse_dict)