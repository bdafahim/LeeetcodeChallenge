class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return false;
        string_s_to_t_map = {}
        string_t_to_s_map = {}
        
        for i in range(len(s)):
            c1 = s[i]
            c2 = t[i]
            if(c1 in string_s_to_t_map and string_s_to_t_map[c1] != c2):
                return False
            if(c2 in string_t_to_s_map and string_t_to_s_map[c2] != c1):
                return False
            else:
                string_s_to_t_map[c1] = c2
                string_t_to_s_map[c2] = c1
        return True

solution = Solution()
s = "egg"
t = "add"
result = solution.isIsomorphic(s,t)

print(result)            
                
