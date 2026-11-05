class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0

        numSet = set(nums)
        longest = 0

        for num in nums:

            count = 1
            
            if (num - 1) in numSet:
                continue
          
            while (num + count) in numSet:
                    count += 1

            longest = max(count, longest)
        return longest
        



        
       
            
