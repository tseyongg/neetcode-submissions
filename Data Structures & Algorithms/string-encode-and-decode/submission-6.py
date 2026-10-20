class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for word in strs:
            word_count = str(len(word))
            s += (word_count + "#" + word)
        return s

    def decode(self, s: str) -> List[str]:
        out = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            wordlen = int(s[i:j])

            word = s[j + 1: j + 1 + wordlen]
            out.append(word)
            i = (j + 1 + wordlen)
        return out