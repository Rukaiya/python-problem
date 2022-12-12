nums = [1,7,3,6,5,6]
sum = sum(nums)
left = 0
right = 0
for index, val in enumerate(nums):
    right = sum - left - val
    if left == right:
        print(index)
    left += val

print(-1)