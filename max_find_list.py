'''
finding max in a list
'''


def find_max(nums):
    if not nums:          # empty list?
        return None

    current = nums[0]     # start with the first number

    for n in nums[1:]:    # walk the rest of the list
        if n > current:
            current = n   # found something bigger

    return current


# try it
print(find_max([3, 7, 2, 9, 4]))   # 9
print(find_max([5]))               # 5
print(find_max([]))                # None
