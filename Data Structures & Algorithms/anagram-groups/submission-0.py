class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictgroups = defaultdict(list)
        for x in strs:
            key = ''.join(sorted(x))
            dictgroups[key].append(x)
        return list(dictgroups.values())
                
        