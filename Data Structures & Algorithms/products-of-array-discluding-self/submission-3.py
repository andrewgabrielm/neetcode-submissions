class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #brute force
        # n = len(nums)
        # output = [None]*n
        
        # for i in range(n):
        #     prod = 1
        #     for j in range(n):
        #         if j != i:
        #             prod *= nums[j]
        #     output[i] = prod
        # return output
        ## prefix and suffix
        n = len(nums)
        pref = [0]*n
        suff = [0]*n
        output = [0]*n

        pref[0] = 1
        suff[n-1] = 1

        for i in range(1,n):
            pref[i] = nums[i-1] * pref[i-1]
        for i in range(n-2,-1,-1):
            suff[i] = suff[i+1] * nums[i+1]

        for i in range(n):
            output[i] = pref[i]* suff[i]
        return output