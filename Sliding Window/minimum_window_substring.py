class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """ Sliding Window """
        window, count_t = {}, {}

        for i in range(len(t)):
            count_t[t[i]] = 1 + count_t.get(t[i], 0)
        
        need = len(count_t)
        have = 0
        res_len = float('inf')
        res = ""
        l, r = 0, 0

        while r < len(s):
            window[s[r]] = 1 + window.get(s[r], 0)

            if s[r] in count_t and count_t[s[r]] == window[s[r]]:
                have += 1
            
            while need == have and l <= r:
                if res_len > (r-l+1):
                    res = s[l:r+1]
                
                if s[l] in count_t and count_t[s[l]] == window[s[l]]:
                    have -= 1
                
                window[s[l]] -= 1
                l += 1
            else:
                r += 1
        
        return res

