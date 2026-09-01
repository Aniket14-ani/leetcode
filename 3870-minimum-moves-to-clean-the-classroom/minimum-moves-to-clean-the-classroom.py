from collections import deque

class Solution:
    def minMoves(self, classroom, energy):
        m = len(classroom)
        n = len(classroom[0])

        start = None
        litter = {}

        
        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    start = (i, j)
                elif classroom[i][j] == 'L':
                    litter[(i, j)] = len(litter)

        k = len(litter)
        target = (1 << k) - 1

        
        q = deque()
        q.append((start[0], start[1], 0, energy))

        
        best = {}
        best[(start[0], start[1], 0)] = energy

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        moves = 0

        while q:
            for _ in range(len(q)):
                r, c, mask, en = q.popleft()

                if mask == target:
                    return moves

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if not (0 <= nr < m and 0 <= nc < n):
                        continue

                    if classroom[nr][nc] == 'X':
                        continue

                    
                    if en == 0:
                        continue

                    new_en = en - 1
                    new_mask = mask

                    if classroom[nr][nc] == 'L':
                        idx = litter[(nr, nc)]
                        new_mask |= (1 << idx)

                    if classroom[nr][nc] == 'R':
                        new_en = energy

                    state = (nr, nc, new_mask)

                    if state not in best or new_en > best[state]:
                        best[state] = new_en
                        q.append((nr, nc, new_mask, new_en))

            moves += 1

        return -1