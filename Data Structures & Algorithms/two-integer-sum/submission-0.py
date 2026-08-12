class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # approach #1, iterate over nums with 2 loops, we'd have O(n) time complexity but O(1) space, direct comparisons

        # approach #2, optimal, keep a hashmap of seen int and its index, we iterate over the nums, and we check the hashmap for the number we'd need to get to the sum and then we can return the 2 index, index of current and dict[target-current] = index.

        seen = dict()

        for i, num in enumerate(nums):
            looking_for = target - num
            if looking_for in seen:
                return [seen[looking_for], i]
            else:
                seen[num] = i
