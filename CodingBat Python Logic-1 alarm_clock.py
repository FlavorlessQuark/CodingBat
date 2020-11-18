def alarm_clock(day, vacation):
  wd = "7:00" if not vacation else "10:00"
  we = "10:00" if not vacation else "off"
  return we if day == 0 or day == 6 else wd
