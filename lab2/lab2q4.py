from re import X
import numpy as np
import copy
import seaborn as sns
import matplotlib.pyplot as plt
import string

def possible(grid,y,x):
  l=len(grid)
  for i in range(l):
    if grid[y][i]==1:
      return False
  for i in range(l):
    if grid[i][x]==1:
      return False
  for i in range(l):
    for j in range(l):
      if grid[i][j]==1:
        if abs(i - y) == abs(j - x):
          return False
  return True

def solve(grid):
  l=len(grid)
  for y in range(l):
    for x in range(l):
      if grid[y][x]==0:
        if possible(grid,y,x):
          grid[y][x]=1
          solve(grid)

          if sum(sum(a) for a in grid)==l:
            return grid
          grid[y][x]=0
  return grid

def plot(grid):
  l=len(grid)
  Ly=list(range(1,l+1))[::-1]
  ly = [str(i) for i in Ly]
  Lx=list(string.ascii_uppercase)
  lx=Lx[:l]
  plt.close('all')
  sns.set(font_scale = 2)
  plt.figure(figsize=(10,10))
  ax = plt.gca()
  ax.set_aspect(1)

  sns.heatmap(Solution,linewidths=.8,cbar=False,linecolor='black',cmap='Accent',center=0.4,xticklabels=lx,yticklabels=ly)
  plt.show()

position = input("enter queen's position (eg.A3) : ")
vertical = 0-(int(position[1])-8)
horizontal = ord(position[0].upper())-65

if(horizontal<0 or horizontal>8 or vertical<0 or vertical>8):
  print("ERROR, input position is out of bounds")
  exit(1)

N=8
grid=np.zeros([N,N],dtype=int)
grid[vertical][horizontal]=1
grid=grid.tolist()

print('Solving {} by {} Chess Board\n'.format(N,N))
Solution = solve(copy.deepcopy(grid))
print(np.matrix(Solution))
plot(grid)

