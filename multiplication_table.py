# multiplication table from 1 to 10 using single loop
from itertools import product

for i, j in product(range(1, 11), range(1, 11)):

    print(i*j, end=" ")
    if j == 10: print("\n")