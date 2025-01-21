class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_map, s_map = {}, {}

        for i in range(len(t)):
            t_map[t[i]] = 1 + t_map.get(t[i], 0)
        
        # print(t_map.items())
        
        need = len(t_map)
        have = 0
        
        res = ""
        res_len = float('inf')

        for i in range(len(s)):
            have = 0

            for j in range(i, len(s)):
                c = s[j]
                s_map[c] = 1 + s_map.get(c, 0)

                if c in t_map and t_map[c] == s_map[c]:
                    have += 1
                
                if have == need and (j-i+1) < res_len:
                    res = s[i:j+1]
                    res_len = j-i+1
                    break

        return res


s="ADOBECODEBANC"
t="ABC"

sol = Solution()
results = sol.minWindow(s, t)

            