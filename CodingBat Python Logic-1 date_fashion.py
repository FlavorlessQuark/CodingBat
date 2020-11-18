def date_fashion(you, date):
  x = 0 if (you &lt;= 2 or date &lt;= 2) else 2 if (you &gt;= 8 or date &gt;= 8) else 1
  return x