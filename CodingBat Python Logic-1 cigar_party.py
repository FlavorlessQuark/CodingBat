def cigar_party(cigars, is_weekend):
  return True if is_weekend and cigars &gt;= 40 or (not is_weekend and cigars &gt;= 40 and cigars &lt;= 60) else False
