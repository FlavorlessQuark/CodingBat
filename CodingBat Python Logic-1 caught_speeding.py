def caught_speeding(speed, is_birthday):
  mod = 0 if not is_birthday else 5
  
  return 0 if speed &lt;=  60 + mod else 1 if 61 + mod &lt;= speed &lt;= 81 + mod else 2
