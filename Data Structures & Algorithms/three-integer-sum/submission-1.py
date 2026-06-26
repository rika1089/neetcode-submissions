class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        SET = set()

        for i in range(n) :
            HASH  = set()
            for j in range(i+1,n) :
                rem = -(nums[i]+nums[j])

                if rem in HASH :
                    SET.add(tuple(sorted([nums[i],nums[j],rem])))
                
                HASH.add(nums[j])
        return [list(lst) for lst in SET]