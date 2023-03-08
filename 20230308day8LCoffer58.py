class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:

        new = s[n::] + s[0:n]
        return new

