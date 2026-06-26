class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs :
            return [[]]

        def isAnagram(s1,s2) :
            if len(s1) != len(s2) :
                return False
            return sorted(s1) == sorted(s2)

        n = len(strs)
        grp = [0]*n
        category = 1
        ans = []

        for i in range(n) :
            if grp[i] != 0 :
                continue
            current_grp = [strs[i]]
            grp[i] = category

            for j in range(i+1,n) :
                if grp[j]==0 and isAnagram(strs[i],strs[j]) :
                    current_grp.append(strs[j])
                    grp[j] = category
                    
            
            ans.append(current_grp)
            category += 1


        return ans
                

