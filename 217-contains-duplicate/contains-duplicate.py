class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        visted = set()
        for i in nums:
            if i in visted: return True
            visted.add(i)
        return False
        