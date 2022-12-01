class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hsmap = {}
        ws = 0
        max_len = 0
        for we in range(len(s)):
            curr_str = s[we]
            if curr_str in hsmap: 
                if ws <= hsmap[curr_str]:
                    ws = hsmap[curr_str]+1
            hsmap[curr_str]=we
            if max_len <= we-ws+1 :
                max_len = we - ws +1
        return max_len
                
                