class Solution:
    def groupAnagrams(self, strs: list):
        output = []
        while len(strs) != 0:
            buffer = [strs[0]]
            letters = list(strs[0])
            glossary = {l: letters.count(l) for l in letters}
            for i in range(1, len(strs)):
                flag = True
                if len(strs[i]) != len(letters):
                    continue
                else:
                    for letter in strs[i]:
                        if letter not in glossary.keys():
                            flag = False
                            break
                        else:
                            n = strs[i].count(letter) 
                            if n != glossary[letter]:
                                flag = False
                                break
                if flag == True:
                    buffer.append(strs[i])
            
            for word in buffer:
                strs.remove(word)

            output.append(buffer)
        
        return output

