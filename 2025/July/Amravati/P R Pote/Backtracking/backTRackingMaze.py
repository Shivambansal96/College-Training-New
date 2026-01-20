maze = [
    ['S', '.', '.', '.'],
    ['#', '#', '.', '#'],
    ['.', '.', '.', '#'],
    ['.', '#', '.', 'E']
]

n = len(maze)
path = []

def is_safe(x, y, visited):
    return 0 <= x < n and 0 <= y < n and maze[x][y] != '#' and not visited[x][y]

def solve(x, y, visited):
    if maze[x][y] == 'E':
        path.append((x, y))
        return True
    
    visited[x][y] = True
    path.append((x, y))

    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  # right, down, left, up
        new_x, new_y = x + dx, y + dy
        if is_safe(new_x, new_y, visited):
            if solve(new_x, new_y, visited):
                return True

    path.pop()  # backtrack
    return False

visited = [[False]*n for _ in range(n)]
solve(0, 0, visited)

# Print final path
for i in range(n):
    row = ""
    for j in range(n):
        if (i, j) in path:
            if maze[i][j] not in ['S', 'E']:
                row += 'P '
            else:
                row += maze[i][j] + ' '
        else:
            row += maze[i][j] + ' '
    print(row)
