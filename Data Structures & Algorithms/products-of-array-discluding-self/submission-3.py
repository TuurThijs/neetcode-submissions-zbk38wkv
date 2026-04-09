class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        elem_to_skip = 0
        
        for skip_index in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if j == skip_index:
                    continue
                product *= nums[j]
            output.append(product)
        return output