"""
Iterates the unordered portion of the list and select the minimum/maximum element. Then swap it
to the front. Sorts the list inplace. Time: O(n^2), Space: O(1)
"""
from typing import List

def selection_sort(nums: List[int]):
    for i in range(len(nums)):
        min_index = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j
        
        nums[min_index], nums[i] = nums[i], nums[min_index]

if __name__ == "__main__":
    l = [3,2.43,2.3,34,23,5345,345,23,43,56,7,231,435,56,2,0,-2,-1,-4]
    print(l)
    
    selection_sort(l)
    assert l == list(sorted(l))
    print(l)