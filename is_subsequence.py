# Author: Christopher Boyd
# GitHub username: CtheBoyd
# Date: 7/18/2022
# Description:  Recursive function that takes two string parameters and returns True if the first string is a
# subsequence of the second string, but returns False otherwise.
#

def is_subsequence(a1, b1):
    """Recursive function that takes two string parameters and returns True if the first string is a
         subsequence of the second string, but returns False otherwise."""
    if not a1:
        return True
    lp = b1.find(a1[0])
    if lp == -1:
        return False
    else:
        return is_subsequence(a1[1:], b1[lp+1:])




