class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        
        for i in range(len(nums)):
            complement = target - nums[i]
            complement_index = hashmap.get(complement)
            if complement_index is not None and complement_index > i:
                return [i,complement_index]

            




