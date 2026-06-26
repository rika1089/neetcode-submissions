class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        ans = []

        for num in nums :
            if num not in count :
                count[num] = 1
            else :
                count[num] += 1

        # for key,val in count.items() :
        #     if val>=k :
        #         ans.append(key)

        # return ans
        sorted_count = sorted(count.items(), key=lambda x:x[1], reverse=True)

        ans = [item[0] for item in sorted_count[:k]]

        return ans