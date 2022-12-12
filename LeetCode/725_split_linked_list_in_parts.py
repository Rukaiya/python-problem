head = [1,2,3]
k = 3
list_length = len(head)
part_size = int(list_length / k) if list_length > k else 1
print(f'part size is: {part_size}')
list = []
start = 0
for i in range(0, list_length, part_size):
    list.append(head[start: start+part_size])
    start += part_size
    print(f'start size is: {start}')

len_remaining = k - len(list) if k > list_length else 0
empty_list = [[] for l in range(len_remaining)]
list.extend(empty_list)
print(list)