class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Step 1: Make dictionary with default empty list
        Step 2: iterate through the list.
        Step 3: get the sorted word as key 
        Step 4: check key in groups dict
        
        """
        groups = defaultdict(list)
        for word in strs:
            key = ''.join(sorted(word))
            groups[key].append(word)
        return list(groups.values())
                

