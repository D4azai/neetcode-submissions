class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        Size_S = len(s)
        Size_T = len(t)

        if Size_S != Size_T:
            return False

        count_s = {}
        count_t = {}

        for i in s:
            if i in count_s:
                count_s[i] += 1
            else:
                count_s[i] = 1

        for i in t:
            if i in count_t:
                count_t[i] += 1
            else:
                count_t[i] = 1

        return count_s == count_t
