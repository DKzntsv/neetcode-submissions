class Solution:
    def isValid(self, s: str):
        stack = []
        open_parantheses = ['(', '{', '[']
        closed_parentheses_map = {
            "(" : ")",
            "{" : "}",
            "[" : "]"
        }

        if s.count('(') != s.count(")") or s.count('{') != s.count("}") or s.count('[') != s.count("]"):
            return False

        for paren in s:
            if paren in open_parantheses:
                stack.append(paren)
                continue

            if not stack:
                return False

            else:
                if closed_parentheses_map[stack[-1]] == paren:
                    stack.pop()
                    continue
                else:
                    return False

        return True