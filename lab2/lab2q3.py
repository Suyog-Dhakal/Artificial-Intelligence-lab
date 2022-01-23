import numpy as np
import copy
import seaborn as sns
import matplotlib.pyplot as plt
import string

def possible(grid, x, y):
    l = len(grid)
    for i in range(l):
        if grid[x][i] == 1:
            return False
    for i in range(l):
        if grid[i][y] == 1:
            return False
    for i in range(l):
        for j in range(l):
            if grid[i][j] == 1:
                if (abs(i-x) == abs(j-y)):
                    return False
    return True


def solve(grid):

    l = len(grid)

    for x in range(l):
        for y in range(l):
            if grid[x][y] == 0:
                if (possible(grid, x, y)):
                    grid[x][y] = 1
                    solve(grid)
                    if (sum(sum(a) for a in grid) == 8):
                        return grid
                    grid[x][y] = 0
    return grid


def plot(grid):
    l = len(grid)
    Ly = list(range(1, l+1))[::-1]
    ly = [str(i) for i in Ly]
    Lx = list(string.ascii_uppercase)
    lx = Lx[:8]

    plt.close('all')
    sns.set(font_scale=2)
    plt.figure(figsize=(10, 10))
    ax = plt.gca()
    ax.set_aspect(1)

    sns.heatmap(Solution, linewidths=.8, cbar=False, linecolor='black',
                cmap='Accent', center=0.4, xticklabels=lx, yticklabels=ly)
    plt.show()


N = 8
grid = np.zeros([N, N], dtype=int)
grid[3][3] = 1
grid = grid.tolist()

print('Solving {} by {} Chess Board\n'.format(N, N))
Solution = solve(copy.deepcopy(grid))
print(np.matrix(Solution))
plot(grid)