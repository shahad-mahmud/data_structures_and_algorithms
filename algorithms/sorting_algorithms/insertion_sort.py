"""
Iterates the unordered portion of the list and select the out of order element. Then swap it
iteratively until the elements is in the relative right position. Sorts the list inplace. 
Time: O(n^2), Space: O(1).
"""
from typing import List

def insertion_sort(nums: List[int]):
    for i in range(len(nums)):
        j = i
        while j > 0 and nums[j] < nums[j-1]:
            nums[j], nums[j-1] = nums[j-1], nums[j]
            j-=1

if __name__ == "__main__":
    l = [3,2.43,2.3,34,23,5345,345,23,43,56,7,231,435,56,2,0,-2,-1,-4]
    print(l)
    
    insertion_sort(l)
    assert l == list(sorted(l))
    print(l)