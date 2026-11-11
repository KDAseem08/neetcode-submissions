class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = ["".join(sorted(word)) for word in strs]
        freq_dist = {}
        for i in range(0,len(strs)):
            if freq_dist.get(sorted_strs[i]) is None:
                freq_dist[sorted_strs[i]] = [strs[i]]
            else:
                freq_dist[sorted_strs[i]].append(strs[i])
        

        return list(freq_dist.values())
          
