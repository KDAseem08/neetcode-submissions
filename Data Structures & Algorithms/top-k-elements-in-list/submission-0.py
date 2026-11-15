from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for i in range(len(nums)):
            d[nums[i]] += 1
        
        thresh = sorted(d.values(),reverse = True)[k-1]

        result = []
        for key,value in d.items():
            if value >= thresh:
                result.append(key)
        
        return result
