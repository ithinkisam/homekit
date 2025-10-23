from domain.unit import Unit

class Units:
  none = Unit("None", "")
  day = Unit("Day", "d")
  week = Unit("Week", "w")
  month = Unit("Month", "m")
  year = Unit("Year", "y")
  day_of_week = Unit("DayOfWeek", "DoW")
  day_of_month = Unit("DayOfMonth", "DoM")
  week_of_month = Unit("WeekOfMonth", "WoM")
  start_of_week = Unit("StartOfWeek", "SoW")
  start_of_month = Unit("StartOfMonth", "SoM")
  start_of_year = Unit("StartOfYear", "SoY")
  end_of_week = Unit("EndOfWeek", "EoW")
  end_of_month = Unit("EndOfMonth", "EoM")
  end_of_year = Unit("EndOfYear", "EoY")

  values = [
    day,
    week,
    month,
    year,
    day_of_week,
    day_of_month,
    week_of_month,
    start_of_week,
    start_of_month,
    start_of_year,
    end_of_week,
    end_of_month,
    end_of_year
  ]

  def by_value(self, value):
    return next((u for u in self.values if u.value == value), None)
