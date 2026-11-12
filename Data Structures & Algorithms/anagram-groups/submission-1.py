# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         a = defaultdict(list)
#         for word in strs:
#             sorted_word = ''.join(sorted(word))
#             a[sorted_word].append(word)

#         return list(a.values())

from collections import defaultdict, Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a = defaultdict(list)
        
        for word in strs:
            # Count the letters, sort them, and turn into a tuple key
            key = tuple(sorted(Counter(word).items()))
            a[key].append(word)
            
        return list(a.values())