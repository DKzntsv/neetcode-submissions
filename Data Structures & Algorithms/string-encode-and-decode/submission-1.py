class Solution:

    def encode(self, strs: list):
        s = ''
        for string in strs:
            s += f'{len(string)}#{string}'
        return s
    
    def decode(self, s: str):
        strs = []
        length, s_buffer = '', ''
        i = 0
        while i < len(s):
            while s[i] != '#':
                length += s[i]
                i += 1
            length = int(length)
            s_buffer += s[i+1: i+length+1]
            i += length + 1
            strs.append(s_buffer)
            length, s_buffer= '', '' 
               
            # else: 
            #     s_buffer += s[i+1 : i+int(length)+1]
            #     strs.append(s_buffer)
            #     s = s[i+int(length)+1:]
            #     length = ''
            #     s_buffer = ''
            #     i = 0
        return strs
    