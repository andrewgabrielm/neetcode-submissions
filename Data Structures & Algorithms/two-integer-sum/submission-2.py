class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """ 
        Two Sum problem
        Brute force:
        - 2 for loops 
        - ith +  i+1th equals target

        """
        # n= len(nums)
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]

        # return []
        indices = {}
        for i,n in enumerate(nums):
            indices[n] = i

        for i,n in enumerate(nums):
            diff = target - nums[i]
            if diff in indices and indices[diff] != i:
                return [i, indices[diff]]
        return []
        