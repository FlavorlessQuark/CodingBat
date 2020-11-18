def squirrel_play(temp, is_summer):
  u_bound = 90 if not is_summer else 100
  return True if 60 &lt;= temp &lt;=u_bound else False              
