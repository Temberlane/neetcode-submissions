class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # worst case O(n) iterate through the entire array, with O(n) space with n = len(nums)
        seen = set()
        for element in nums:
            if element in seen:
                return True
            else:
                seen.add(element)
        return False

            
