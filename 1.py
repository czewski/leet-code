class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for idx in range(n):
            for idy in range(n):
                if nums[idx]+nums[idy] == target: 
                    if idx != idy:
                        return [idx,idy]
                        break