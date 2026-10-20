class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for string in strs:
            strlen = len(string)
            s = s + str(strlen) + "#" + string
        return s


    def decode(self, s: str) -> List[str]:
        i = 0
        out = []
        while i < len(s):
            #read num
            j = i
            while s[j] != "#":
                j += 1
            wordlen = int(s[i:j])

            #read the word
            word = s[j+1:j+1+wordlen]
            out.append(word)

            #move foward
            i = j + 1 + wordlen
        return out



            


