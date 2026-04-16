class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouping_key = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word not in grouping_key:
                grouping_key[sorted_word] = []
            grouping_key[sorted_word].append(word)
        return list(grouping_key.values())