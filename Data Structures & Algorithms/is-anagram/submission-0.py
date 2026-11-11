class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_freq_dict = {}
        t_freq_dict = {}
        
        for i in range(0,len(s)):
            if s_freq_dict.get(s[i]) is None:
                s_freq_dict[s[i]] = 0 
            else:
                s_freq_dict[s[i]] += 1
        
            if t_freq_dict.get(t[i]) is None:
                t_freq_dict[t[i]] = 0 
            else:
                t_freq_dict[t[i]] += 1
        
        return s_freq_dict == t_freq_dict