class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        tot_fruit = 0
        rot_fruit = set()
        q = deque()
        rows, cols = len(grid), len(grid[0])

        def fruit_check(r,c):
            if r < 0 or c < 0 or r >= rows or c >= cols or (r,c) in rot_fruit or grid[r][c] != 1:
                return
            rot_fruit.add((r,c))
            q.append((r,c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                    rot_fruit.add((r,c))
                    tot_fruit += 1
                elif grid[r][c] == 1:
                    tot_fruit += 1
        minutes = 0
        # Process layer-by-layer
        while q:
            rotten_added = False
            for _ in range(len(q)):
                r, c = q.popleft()

                prev_len = len(q)
                fruit_check(r, c + 1)
                fruit_check(r, c - 1)
                fruit_check(r + 1, c)
                fruit_check(r - 1, c)
                if len(q) > prev_len:
                    rotten_added = True

            if rotten_added:
                minutes += 1

        if len(rot_fruit) != tot_fruit:
            return -1
        else:
            return minutes
