class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        A=list(s)
        for i in t:
            if i in A:
                A.remove(i)
            else:
                return i
