class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        i = 0
        indices = {}

        for i,n in enumerate(nums) :
            indices[n] = i
        
        for i,n in enumerate(nums) :
            rem = target - n
            if rem in indices and indices[rem] != i :
                return [i,indices[rem]]
        return []
                
        
        
