from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # approach #1 iterate over strs, and check for anagrams matching,
        # would be very inefficient

        # approach #2, have a set of Counters of strs, if 2 counters are equal, they are anagrams. 
        # iterate over each then sort have keys its n^2 log n time complexity
        seen = {} # key : sorted, value : the strings in an array
        for word in strs:
            cur_key = "".join(sorted(word))
            if cur_key in seen:
                seen[cur_key].append(word)
            else:
                seen[cur_key] = [word]
            
        output = []
        for anagram_group in seen.keys():
            output.append(seen[anagram_group])
        return output