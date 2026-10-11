
class Solution:
    def longestCommonPrefix(self, strs):
        shortest = min(len(word) for word in strs)
        prefix = ""

        for i in range(shortest):
            for word in strs:
                if word[i] != strs[0][i]:
                    return prefix

            prefix += strs[0][i]

        return prefix
