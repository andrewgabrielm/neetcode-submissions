class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
      
        seen = {}
        for num in nums:
            if num not in seen:
                seen[num] = 1
            else: return True
       
        return False

        #sorting approach
        # n = len(nums)
        # nums.sort()
        # for i in range(1,n):
        #     if nums[i] == nums[i-1]:
        #         return True
        # return False