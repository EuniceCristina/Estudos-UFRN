mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in range(3):
  sm = 0
  for j in range(3):
    sm += mat[i][j]
  print('[', i+1, ']', sm)