class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        d = {key: val for key, val in knowledge}
        
        res = []
        in_bracket = False
        key_buf = []
        
        for char in s:
            if char == '(':
                in_bracket = True
                key_buf = []
            elif char == ')':
                in_bracket = False
                key = "".join(key_buf)
                res.append(d.get(key, "?"))
            else:
                if in_bracket:
                    key_buf.append(char)
                else:
                    res.append(char)
                    
        return "".join(res)