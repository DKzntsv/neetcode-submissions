class Solution:

    def encode(self, strs: list):
        enc = ''
        for s in strs:
            enc += f'{len(s)}#{s}'
        return enc
    
    def decode(self, s: str):
        length, s_buffer = '', ''
        dec = []
        i = 0
        while i < len(s):
            while s[i] != "#":
                length += s[i]
                i += 1
            length = int(length)
            s_buffer += s[i+1:i+length+1]
            i += length+1
            dec.append(s_buffer)
            length, s_buffer = '', ''

        return dec