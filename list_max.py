# Author: Christopher Boyd
# GitHub username: CtheBoyd
# Date: 7/18/2022
# Description: Recursive function that takes as its parameter a list of numbers and returns the maximum value in the list.
#

def list_max(nums):
    """a recursive function that takes as its parameter a list of numbers and returns the maximum value in the list."""
    if len(nums) == 1:
        return nums[0]
    else:
        number = list_max(nums[1:])
        return number if number > nums[0] else nums[0]

#nums = [1,2,-65,3,-1,6,45,2000, 6, 0]
#print(list_max(nums))
