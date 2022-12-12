nums  = [1, 2, 3, 4]
returnList = [nums[0]]
# l1 = lambda c, x: [c+ (x - 1) for x in nums[1:]]
c = 0
l2 = [c := c + x for x in nums]
print(l2)