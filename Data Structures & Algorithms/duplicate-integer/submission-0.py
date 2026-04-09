class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        singles = []
        for i in nums:
            if not i in singles:
                singles.append(i)
        if nums == singles:
            return False
        else: 
            return True
