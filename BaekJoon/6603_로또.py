from itertools import combinations

nums = [8, 1, 2, 3, 5, 8, 13, 21, 34]

permute = combinations(nums[1:], 6)
for i in permute:
    print(i)
