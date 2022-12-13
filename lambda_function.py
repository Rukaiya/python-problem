# Add two lists using map and lambda

numbers1 = [1, 2, 3, 6]
numbers2 = [4, 5, 6]

result = list(map(lambda x, y: x + y, numbers1, numbers2))
print(result)

format_numeric = lambda num: f"{num:e}" if isinstance(num, int) else f"{num:,.2f}"

print("Int formatting:", format_numeric(1000000))
print("float formatting:", format_numeric(999999.789541235))

# people above 18 yrs
ages = [13, 90, 17, 59, 21, 60, 5]
adults = list(filter(lambda age: age > 18, ages))

print(adults)