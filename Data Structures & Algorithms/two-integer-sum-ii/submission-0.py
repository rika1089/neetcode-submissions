class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hash_map = {}

        for i in range(len(numbers)) :
            rem = target-numbers[i]
            if rem in hash_map :
                return [hash_map[rem]+1,i+1]

            else :
                hash_map[numbers[i]] = i
        return []

        