class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # s = re.sub(r'[^a-zA-Z0-9]', '', s)
        # s = s.lower()
        # n = len(s)
        # i = 0 
        # j = n-1
        # # if n == 0:
        # #     return False
        
        # while i < j:
        #     if s[i] != s[j]:
        #         return False
        #     else:
        #         i+=1
        #         j-=1
        # return True
        i ,j = 0, len(s)-1
        s = s.lower()
        while i<j:
            while i<j and not s[i].isalnum():
                i+=1
            while i<j and not s[j].isalnum():
                j-=1
            if s[i] != s[j]:
                return False
            i,j = i+1,j-1
        return True

