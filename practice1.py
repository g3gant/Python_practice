class Solution:
  
  def maxConnected(self, grid):
    maxCount = 0
    for y in range(0, len(grid)):
      for x in range(0, len(grid[y])):
        count = self.__traverseHelper(grid, x, y, 0, {})
        maxCount = max(count, maxCount)
    return maxCount

  def __traverseHelper(self, grid, x, y, count, seen):
    
    #CHECKING IF THE CELL ALREADY HAS BEEN SEEN, THEN DON'T COUNT
    key = (x,y)
    if seen.get(key) != None:
      return 0
    seen[key] = True

    color = grid[x][y]

    neighbors = self.__getNeighbors(grid, x, y)
    
    sum = 1
    for point in neighbors:
      i = point[0]
      j = point[1]
      if grid[i][j] != color:
        continue
      
      seen[key] = True
      sum += self.__traverseHelper(grid, i, j, 1, seen)
      #sum += self.__traverseHelperIterative(grid, i, j, 1, seen)
    return sum

  def __getNeighbors(self, grid, x, y ):
    coords = []
    neighbors = [
      [-1, 0],
      [0, -1],
      [1, 0],
      [0, 1],
    ]
    
    for n in neighbors:
      coordX = x + n[0]
      coordY = y + n[1]
      if coordX < 0 or coordY < 0 or coordY >= len(grid) or coordX >= len(grid[0]):
        continue
      coords.append([coordX, coordY])
    return coords
  
grid = [
['r', 'g', 'r'],
['g', 'g', 'g'],
['g', 'g', 'r']
]
sol = Solution()
print (sol.maxConnected(grid))