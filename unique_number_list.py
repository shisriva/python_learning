'''
Write unique(nums) that returns a new list with duplicates removed, first time each number appears kept.

'''


def unique(nums):
    new = []
    for numbers in nums:
        if numbers not in new:   # only add first time we see it
            new.append(numbers)
    return new


print(unique([1, 2, 2, 3, 1]))   # [1, 2, 3]
print(unique([5, 5, 5]))         # [5]
print(unique([]))                # []
