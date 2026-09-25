class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
  
        stack = []
        groups = []
        cur = {""}

        for char in expression:
            if char.isalpha():
                
                cur = {s + char for s in cur}
            elif char == '{':
                
                stack.append((groups, cur))
                groups, cur = [], {""}
            elif char == ',':
               
                groups.extend(cur)
                cur = {""}
            elif char == '}':
                
                groups.extend(cur)
                scope_set = set(groups)
            
                prev_groups, prev_cur = stack.pop()
               
                cur = {a + b for a in prev_cur for b in scope_set}
                groups = prev_groups

        groups.extend(cur)
        return sorted(list(set(groups)))