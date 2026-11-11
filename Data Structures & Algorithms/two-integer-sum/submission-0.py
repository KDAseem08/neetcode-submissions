class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            if nums[i] in hashmap.values():
                key = [key for key,value in hashmap.items() if value == nums[i]][0] 
                return [min(key,i),max(key,i)]
            else:
                hashmap[i] = target - nums[i]

