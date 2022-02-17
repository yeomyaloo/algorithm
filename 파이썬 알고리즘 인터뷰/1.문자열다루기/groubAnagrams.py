import collections


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrames = collections.defaultdict(list)

        for word in strs:
            anagrames[''.join(sorted(word))].append(word)

        return list(anagrames.values())