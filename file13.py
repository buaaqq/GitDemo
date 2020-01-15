class Solution(object):
    def romanToInt(self, s):
        lookup = {'I': 1,
                  'V': 5,
                  'X': 10,
                  'L': 50,
                  'C': 100,
                  'D': 500,
                  'M': 1000}

        y = 0

        for i in range(len(s)):
            if i > 0 and lookup[s[i]] > lookup[s[i - 1]]:
                y = y + lookup[s[i]] - 2 * lookup[s[i - 1]]
            else:
                y = y + lookup[s[i]]

        return y