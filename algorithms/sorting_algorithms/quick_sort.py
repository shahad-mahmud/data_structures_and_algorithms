import random
from typing import List


def swap(nums, i, j):
    nums[i], nums[j] = nums[j], nums[i]


def divide(nums, low, high):
    pivot = nums[high]
    q = low

    for i in range(low, high):
        if nums[i] <= pivot:
            swap(nums, q, i)
            q += 1

    swap(nums, q, high)
    return q


def random_divide(nums, low, high):
    pivot_index = random.randint(low, high)
    
    swap(nums, high, pivot_index)
    return divide(nums, low, high)

def quick_sort(nums: List[int], low, high) -> List[int]:
    if (high - low + 1) > 1:
        pivot_index = random_divide(nums, low, high)
        quick_sort(nums, low, pivot_index-1)
        quick_sort(nums, pivot_index+1, high)


if __name__ == "__main__":
    nums = [3, 45, 32, 345, 56, 0, 8, -234, 34, -5, -67, 234, -65]
    print(nums)

    quick_sort(nums, 0, len(nums)-1)
    print(nums)
