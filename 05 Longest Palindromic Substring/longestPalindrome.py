
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s

        table = []
        for _ in range(n):
            table.append([False] * n)

        start = 0
        max_len = 1

        for i in range(n):
            table[i][i] = True

        for i in range(n - 1):
            if s[i] == s[i + 1]:
                table[i][i + 1] = True
                start = i
                max_len = 2

        for l in range(3, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1
                if s[i] == s[j] and table[i + 1][j - 1]:
                    table[i][j] = True
                    if l > max_len:
                        start = i
                        max_len = l

        return s[start:start + max_len]

print(Solution().longestPalindrome("babad"))