from collections import defaultdict
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # approach #1, brute force, try to mutate s to become t or vice versa
        # would be very computationally expensive O(n!) we check n x n-1 etc until 1 which is n!

        # approach #2, go through s, check if char is in t, if it is, remove char from t, if we end up with empty t, we can build t from s, would be O(n * m) and O(m) space

        # approach #3, turn s and t into a dict with keys = chars and num = count of chars, then compare the two so we have O(n + m) time and O(26) space (26 keys)

        # def convert_to_dict(cur: str) -> dict:
        #     letter_count = defaultdict(int)
        #     for char in cur:
        #         letter_count[char] += 1
        #     return letter_count
        
        if len(s) != len(t):
            return False
        
        # return convert_to_dict(s) == convert_to_dict(t)
        # use Counter for frequency of elements but default dict is any type.
        return Counter(s) == Counter(t)
