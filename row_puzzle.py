# Author: Christopher Boyd
# GitHub username: CtheBoyd
# Date: 7/18/2022
# Description: Recursive function that takes a list of integers (the row) as a parameter and returns True
# if the puzzle is solvable for that row, but returns False otherwise.
#



def puzzle_solver(nums, list_pos, memo_list):
    """Description: Recursive function that takes a list of integers (the row) as a parameter and returns True
       if the puzzle is solvable for that row, but returns False otherwise."""

    pos_num = nums[list_pos]

    if list_pos == (len(nums) - 1):
        return True
    elif list_pos > (len(nums) - 1):
        return False
    elif pos_num == 0:
        return False
    elif memo_list[list_pos] != 0:
        return False

    move_left = False
    move_right = False
    memo_list[list_pos] = 1

    if (0 <= (list_pos - pos_num)):       #move left is valid
        move_left = puzzle_solver(nums, list_pos - pos_num, memo_list)

    if len(nums) > list_pos + pos_num:   #move right is valid
        move_right = puzzle_solver(nums, list_pos + pos_num, memo_list)

    return move_right or move_left

def row_puzzle(nums):

    memo_list = []
    for list_pos in range(len(nums)):
        memo_list.append(0)
    return puzzle_solver(nums, 0, memo_list)

