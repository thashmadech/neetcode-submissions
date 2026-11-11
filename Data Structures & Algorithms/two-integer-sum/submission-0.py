class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        valMap = {}
        for i,val in enumerate(nums):
            diff = target - val
            if diff in valMap:
                return [valMap[diff],i]
            valMap[val] = i

        # Brute Force
        # for i in range(0, len(nums)-1):
        #     for j in range(i+1, len(nums)):
        #         if nums[i]+nums[j] == target:
        #             return [i,j]

        