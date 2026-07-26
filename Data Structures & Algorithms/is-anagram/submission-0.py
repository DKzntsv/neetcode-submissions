class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        symbols_s, symbols_t  = {}, {}
        for symbol in s:
            if symbol not in symbols_s.keys():
                symbols_s[symbol] = 1
            else:
                symbols_s[symbol] += 1
                 
        for symbol in t:
            if symbol not in symbols_t.keys():
                symbols_t[symbol] = 1
            else:
                symbols_t[symbol] += 1
                 
        return symbols_s == symbols_t
    