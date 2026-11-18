class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = {-1: 1}
        suffix = {len(nums): 1}
        prefix_prod = 1 
        suffix_prod = 1

        for i in range(0,len(nums)):
            prefix_prod *= nums[i]
            prefix[i] = prefix_prod
        
        for j in range(len(nums)-1,-1,-1):
            suffix_prod *= nums[j]
            suffix[j] = suffix_prod

        final_array = [0] * len(nums)
        
        for k in range(0,len(nums)):
            final_array[k] = prefix[k-1] * suffix[k+1]
        
        return final_array
        

