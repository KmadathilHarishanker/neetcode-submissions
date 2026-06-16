class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anag = defaultdict(list)

        for i in strs:

            sortedStr = ''.join(sorted(i))

            anag[sortedStr].append(i)

        return list(anag.values())



        


        