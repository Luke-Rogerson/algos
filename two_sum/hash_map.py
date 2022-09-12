from typing import List

# https://leetcode.com/problems/two-sum/

def twoSum(nums: List[int], target: int) -> List[int]:
  seen = {}
  # iterate thru nums
  for (index, value) in enumerate(nums):
    # check if target - current num is in hash map
    remaining = target - value
    # if it is return 
    if remaining in seen:
      return [index, seen[remaining]]
    
    # set key: num, val: index
    seen[value] = index
    
print(twoSum([2, 7, 11, 15], 9))
