class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        seen = set()
        for i in range(n):
            if nums[i] in seen:
                return True
            seen.add(nums[i])

        return False

        #sorting approach
        # n = len(nums)
        # nums.sort()
        # for i in range(1,n):
        #     if nums[i] == nums[i-1]:
        #         return True
        # return False