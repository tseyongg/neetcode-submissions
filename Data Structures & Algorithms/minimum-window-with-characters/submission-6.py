class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        l = 0
        min_win_len = 10 ** 6
        start_idx = None
        w_dict = {}
        

        t_dict = {}
        
        for char in t:
            t_dict[char] = t_dict.get(char, 0) + 1
        
        have, need = 0, len(t_dict)
        
        # def valid():
        #     for key in t_dict:
        #         if key not in w_dict:
        #             return False
        #         if w_dict[key] < t_dict[key]:
        #             return False
        #     return True

        for r in range(len(s)):
            w_dict[s[r]] = w_dict.get(s[r], 0) + 1

            if s[r] in t_dict and w_dict[s[r]] == t_dict[s[r]]:
                have += 1

            while have == need:
                win_len = r - l + 1
                if s[l] in t_dict and w_dict[s[l]] == t_dict[s[l]]:
                    have -= 1
                
                if win_len < min_win_len:
                    start_idx = l
                    min_win_len = win_len
                w_dict[s[l]] -= 1
                l += 1
        if min_win_len == 10 ** 6: return ""
        return s[start_idx:start_idx + min_win_len]