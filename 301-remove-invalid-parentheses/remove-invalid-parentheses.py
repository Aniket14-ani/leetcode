class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def is_valid(string: str) -> bool:
            count = 0
            for char in string:
                if char == '(':
                    count += 1
                elif char == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0

        queue = [s]
        visited = {s}
        result = []
        found = False

        while queue:
            curr = queue.pop(0)

            if is_valid(curr):
                result.append(curr)
                found = True

            if found:
                continue

            for i in range(len(curr)):
                if curr[i] not in "()":
                    continue
                
                next_str = curr[:i] + curr[i+1:]
                if next_str not in visited:
                    visited.add(next_str)
                    queue.append(next_str)

        return result