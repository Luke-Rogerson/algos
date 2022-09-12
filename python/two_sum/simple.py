from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
       seen = {}
       for i, value in enumerate(nums):
           remaining = target - nums[i]
           
           if remaining in seen:
               return [i, seen[remaining]]
            
           seen[value] = i 
           
print(twoSum([2, 7, 11, 15], 9))
