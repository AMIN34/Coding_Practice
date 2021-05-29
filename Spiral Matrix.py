class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        m, n = len(matrix), len(matrix[0])
        total = m * n
        def dg():
            directions = [(1,0), (0, 1), (-1, 0), (0, -1)]
            for i in itertools.count():
                yield directions[i%4]
        direction = dg()
        d = next(direction)
        p = [-1, 0]
        ans = []
        while len(ans) < total:
            if (not (0 <= (x := p[0] + d[0]) < n and
                     0 <= (y := p[1] + d[1]) < m) or matrix[y][x] == '#'):
                d = next(direction)
                x, y = p[0] + d[0], p[1] + d[1]
            ans.append(matrix[y][x])
            matrix[y][x] = '#'
            p = [x, y]
        return ans