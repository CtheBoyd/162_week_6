# Author: Christopher Boyd
# GitHub username: CtheBoyd
# Date: 7/18/2022
# Description: Recursive function that takes as its parameter a list of numbers. It should return True if the
# elements of the list are strictly decreasing but return False otherwise.
#


def is_decreasing(nums):
    """Recursive function that takes as its parameter a list of numbers. It should return True if the elements of
    the list are strictly decreasing but return False otherwise."""
    if len(nums) <=1 or (len(nums) == 2 and nums[0] >= nums[1]):
        return True

    else:
        if nums[0]>= nums[1]:
            return is_decreasing(nums[1::])

        else:
            return False


