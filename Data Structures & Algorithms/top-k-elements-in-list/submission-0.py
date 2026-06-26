class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        ans = []
        for num in nums :
            if num not in count :
                count[num] = 1
            else :
                count[num] += 1

        sorted_items = sorted(count.items(), key=lambda x: x[1], reverse=True)

        # Step 3: Collect top k elements
        for i in range(k):
            ans.append(sorted_items[i][0])

        return ans
