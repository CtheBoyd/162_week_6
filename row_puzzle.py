# Author: Christopher Boyd
# GitHub username: CtheBoyd
# Date: 7/18/2022
# Description: Recursive function that takes a list of integers (the row) as a parameter and returns True
# if the puzzle is solvable for that row, but returns False otherwise.
#

def puzzle_solver(nums, list_pos, memo=None):
    """ Recursive function that takes a list of integers (the row) as a parameter and returns True
               if the puzzle is solvable for that row, but returns False otherwise."""
    pos_num = nums[list_pos]

    if memo is None:
        memo = []

    if list_pos == (len(nums) - 1):
        return True
    elif list_pos > (len(nums) - 1):
        return False
    elif list_pos in memo:
        return False

    left = right = False
    memo.append(list_pos)

    if (0 <= (list_pos - pos_num)):  # move left is valid
        left = puzzle_solver(nums, list_pos - pos_num, memo)

    if len(nums) > (list_pos + pos_num):  # move right is valid
        right = puzzle_solver(nums, list_pos + pos_num, memo)

    return right or left



def row_puzzle(nums):
    """Function runs the game."""
    return puzzle_solver(nums, 0)




