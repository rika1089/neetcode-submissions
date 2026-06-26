class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = list()

        if not strs :
            return [[]]
        
        n = len(strs)

        grp = [0]*n
        category = 1

        def isAnagram(a,b) :
            if len(a) != len(b) :
                return False
            return sorted(a) == sorted(b)
        
        for i in range(n) :
            if grp[i] == 0 :
                current_grp = [strs[i]]
                grp[i] = category

                for j in range(i+1,n) :
                    if grp[j] == 0 and isAnagram(strs[i],strs[j]) :
                        current_grp.append(strs[j])
                        grp[j] = category
                ans.append(current_grp)
                category += 1
        return ans
                


