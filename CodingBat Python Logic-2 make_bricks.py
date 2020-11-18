def make_bricks(small, big, goal):
   b = goal - ((goal // 5) * 5 if big &gt;= goal // 5 else big * 5)
   return abs(b) &lt;= small and goal // 5 &lt;= goal
  #l = [x + y * 5 for x in range(small + 1) for y in range(big + 1)]
 # return goal in l