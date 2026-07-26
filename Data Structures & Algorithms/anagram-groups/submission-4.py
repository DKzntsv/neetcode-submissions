# class Solution:
#     def groupAnagrams(self, strs: list):
#         output = []
#         while len(strs) != 0:
#             buffer = [strs[0]]
#             letters = list(strs[0])
#             glossary = {l: letters.count(l) for l in letters}
#             for i in range(1, len(strs)):
#                 flag = True
#                 if len(strs[i]) != len(letters):
#                     continue
#                 else:
#                     for letter in strs[i]:
#                         if letter not in glossary.keys():
#                             flag = False
#                             break
#                         else:
#                             n = strs[i].count(letter) 
#                             if n != glossary[letter]:
#                                 flag = False
#                                 break
#                 if flag == True:
#                     buffer.append(strs[i])
            
#             for word in buffer:
#                 strs.remove(word)

#             output.append(buffer)
        
#         return output

# Very inefficient, time complexity O(n^2*m^2) since we are using count() too many times
# Avoid using count() at all costs, it's just a hidden for loop!!!
# Optimal silution is using a hashmap and identifying a 'blueprint' of each word

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1 # ASCII values iteration
            res[tuple(count)].append(s)
        return list(res.values())