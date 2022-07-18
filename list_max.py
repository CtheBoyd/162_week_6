# Author: Christopher Boyd
# GitHub username: CtheBoyd
# Date: 7/18/2022
# Description: Recursive function that takes as its parameter a list of numbers and returns the maximum value in the list.
#

def list_max(nums):
    """a recursive function that takes as its parameter a list of numbers and returns the maximum value in the list."""
    length = len(nums)

    if length == 1:
        return nums

    elif nums[length-1] >= nums[length-2]:
        del nums[length-2]

    elif nums[length-1] <= nums[length-2]:
        del nums[length-1]

    return list_max(nums)

print (list_max([1,2,95754754745,3,1,8,444,2,42425]))
