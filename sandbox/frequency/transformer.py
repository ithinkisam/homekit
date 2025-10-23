from datetime import date
from domain.transformation import Transformation
from domain.units import Units

import arrow

class Transformer:

  def __init__(self, profile = {}):
    self._profile = profile
    
    if "start_of_week" not in self._profile:
      self._profile["start_of_week"] = "MONDAY"

  def transform(self, date: date, transformation: Transformation):
    result = arrow.get(date)

    match transformation.unit:
      case Units.day:
        result = result.shift(days=transformation.amount)
      case Units.week:
        result = result.shift(weeks=transformation.amount)
      case Units.month:
        result = result.shift(months=transformation.amount)
      case Units.year:
        result = result.shift(years=transformation.amount)
      case Units.day_of_week:
        result = result.shift(weekday=transformation.amount)
        # not sure on this one
      case Units.day_of_month:
        result = result.replace(day=transformation.amount)
      case Units.week_of_month:
        result = result.replace(week=transformation.amount)
      case Units.start_of_week:
        result = result.replace(weekday=0)
      case Units.start_of_month:
        result = result.replace(day=0)
      case Units.start_of_year:
        result = result.replace(month=0, date=0)
      case Units.end_of_week:
        result = result.replace(weekday=7)
      case Units.end_of_month:
        result = result.shift(months=+1).shift(days=-1)
      case Units.end_of_year:
        result = result.replace(month=12, date=31)
    
    return result.date()


def test(expected, actual):
  assert expected == actual

if __name__ == "__main__":
  t = Transformer()

  assert date(2023, 11, 3) == t.transform(date(2023, 10, 31), Transformation(3, Units.day))
  assert date(2023, 10, 5) == t.transform(date(2023, 10, 31), Transformation(5, Units.day_of_month))