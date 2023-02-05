class Solution:
    def sortSentence(self, s: str) -> str:
         return " ".join([y[1:][::-1] for y in sorted([x[::-1] for x in s.split(" ")])])
