from collections import Counter, defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # approach #1 iterate over strs, and check for anagrams matching,
        # would be very inefficient

        # approach #2, have a set of Counters of strs, if 2 counters are equal, they are anagrams. 
        # iterate over each then sort have keys its n^2 log n time complexity

        # approach #3, use hashed counters with frozenset (my intuition lol)
        # seen = {} # key : sorted, value : the strings in an array
        # for word in strs:
        #     cur_key = "".join(sorted(word))
        #     if cur_key not in seen:
        #         seen[cur_key] = []    
        #     seen[cur_key].append(word)
            
        # output = []
        # for anagram_group in seen.keys():
        #     output.append(seen[anagram_group])
        # return output

        seen = defaultdict(list)
        
        for word in strs:
            # Counter(word).items() gives dict_items([('a', 2), ('b', 1)])
            # frozenset(...) makes it hashable so it can serve as a dict key
            key = frozenset(Counter(word).items())
            seen[key].append(word)
            
        return list(seen.values())