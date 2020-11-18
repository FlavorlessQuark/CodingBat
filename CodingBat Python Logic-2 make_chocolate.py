def make_chocolate(small, big, goal):
   b = goal - ((goal // 5) * 5 if big &gt;= goal // 5 else big * 5)
   return abs(b) if abs(b) &lt;= small else -1
