import re
import datetime

REGEX_RECURRING = re.compile(r"REC_(\d+)([DWMY])")
RECURRING_UNITS = {
  "D": "day",
  "W": "week",
  "M": "month",
  "Y": "year"
}

REGEX_RELATIVE = re.compile(r"REL_([1-5])_(MON|TUE|WED|THU|FRI|SAT|SUN)_([0-1][0-9])")
ORDINALS = {
  "1": "First",
  "2": "Second",
  "3": "Third",
  "4": "Fourth",
  "5": "Fifth"
}
DAY_OF_WEEK = {
  "MON": "Monday",
  "TUE": "Tuesday",
  "WED": "Wednesday",
  "THU": "Thursday",
  "FRI": "Friday",
  "SAT": "Saturday",
  "SUN": "Sunday"
}
DAY_OF_WEEK_NUM = {
  "MON": 0,
  "TUE": 1,
  "WED": 2,
  "THU": 3,
  "FRI": 4,
  "SAT": 5,
  "SUN": 6
}
MONTH = {
  "01": "January",
  "02": "February",
  "03": "March",
  "04": "April",
  "05": "May",
  "06": "June",
  "07": "July",
  "08": "August",
  "09": "September",
  "10": "October",
  "11": "November",
  "12": "December"
}
UNIT = {
  "W": "week",
  "M": "month",
  "Y": "year"
}

REGEX_FIXED = re.compile(r"FIX_([01][0-9])([0-3][0-9])")

REGEX_RECURRING_RELATIVE = re.compile(r"RECL_(L|[0-3][0-9])([WMY])")

def expand_frequency(freq: str):
  if match := REGEX_RECURRING.match(freq):
    return expand_recurring(freq, match)
  elif match := REGEX_RELATIVE.match(freq):
    return expand_relative(freq, match)
  elif match := REGEX_FIXED.match(freq):
    return expand_fixed(freq, match)
  elif match := REGEX_RECURRING_RELATIVE.match(freq):
    return expand_recurring_relative(freq, match)
  return freq

def expand_recurring(freq: str, match: re.match):
  num = int(match.group(1))
  unit = RECURRING_UNITS[match.group(2)]
  return f"{freq} => Every {num} {unit}s" if num > 1 else f"{freq} => Every {unit}"

def expand_relative(freq: str, match: re.match):
  num = ORDINALS[match.group(1)]
  day_of_week = DAY_OF_WEEK[match.group(2)]
  month = MONTH[match.group(3)]
  return f"{freq} => Every {num.lower()} {day_of_week} of {month}"

def expand_fixed(freq: str, match: re.match):
  month = MONTH[match.group(1)]
  day = ordinal(int(match.group(2)))
  return f"{freq} => {month} {day}"

def expand_recurring_relative(freq: str, match: re.match):
  num = match.group(1)
  day = match.group(2)
  day_word = UNIT[day[-1]].lower()
  return f"Last day of every {day_word}" if num == "L" else f"{ordinal(int(num))} day of every {day_word}"

def ordinal(n: int):
  if 11 <= (n % 100) <= 13:
    suffix = 'th'
  else:
    suffix = ['th', 'st', 'nd', 'rd', 'th'][min(n % 10, 4)]
  return str(n) + suffix

def get_next(freq: str, current: datetime):
  next = current
  if match := REGEX_RECURRING.match(freq):
    next = get_recurring(freq, current, match)
  elif match := REGEX_RELATIVE.match(freq):
    next = get_relative(freq, current, match)
  elif match := REGEX_FIXED.match(freq):
    next = get_fixed(freq, current, match)
  return f"{freq} => {next}"

def get_recurring(freq: str, current: datetime, match: re.match):
  num = int(match.group(1))
  unit = match.group(2)
  increment = datetime.timedelta(days=0)
  if unit == "D":
    increment = datetime.timedelta(days=num)
  elif unit == "W":
    increment = datetime.timedelta(weeks=num)
  elif unit == "M":
    increment = datetime.timedelta(days=(num*30.437))
  elif unit == "Y":
    increment = datetime.timedelta(days=365.25)
  return (current + increment).date()

def get_relative(freq: str, current: datetime, match: re.match):
  year = current.date().year
  month = int(match.group(3))
  day_of_week = DAY_OF_WEEK_NUM[match.group(2)]
  week = int(match.group(1))
  next = datetime.date(year, month, ((week - 1) * 7) + 1)
  while next.weekday() != day_of_week:
    next = next + datetime.timedelta(days=1)
  if next > current.date():
    return next
  # Already passed the date, so roll to next year
  next = datetime.date(year + 1, month, ((week - 1) * 7) + 1)
  while next.weekday() != day_of_week:
    next = next + datetime.timedelta(days=1)
  return next

def get_fixed(freq: str, current: datetime, match: re.match):
  month = int(match.group(1))
  day = int(match.group(2))
  year = current.date().year
  date = datetime.date(year, month, day)
  return date if date > current.date() else datetime.date(year + 1, month, day)

def get_recurring_relative(freq: str, current: datetime, match: re.match):
  num = match.group(1)
  day = match.group(2)
  unit = day[-1] # W, M or Y
  # TODO

if __name__ == "__main__":
  print(expand_frequency("INVALID"))

  print(expand_frequency("REC_1D"))
  print(expand_frequency("REC_2W"))
  print(expand_frequency("REC_6M"))
  print(expand_frequency("REC_1Y"))

  print(expand_frequency("REL_3_WED_01"))
  print(expand_frequency("REL_1_SAT_05"))

  print(expand_frequency("RECL_LW"))
  print(expand_frequency("RECL_LM"))
  print(expand_frequency("RECL_LY"))
  print(expand_frequency("RECL_14M"))

  print(expand_frequency("FIX_0701"))
  print(expand_frequency("FIX_1225"))
  print(expand_frequency("FIX_0101"))

  print()

  now = datetime.datetime.now()
  print(get_next("REC_1D", now))
  print(get_next("REC_2W", now))
  print(get_next("REC_6M", now))
  print(get_next("REC_1Y", now))

  print(get_next("REL_3_WED_01", now))
  print(get_next("REL_3_SAT_05", now))
  print(get_next("REL_4_THU_11", now))

  print(get_next("FIX_0701", now))
  print(get_next("FIX_1225", now))
  print(get_next("FIX_0101", now))
  