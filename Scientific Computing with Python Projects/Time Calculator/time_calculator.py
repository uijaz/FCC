__days = 0
__hours = 0


def convert_12to24_hours(hours, period): # returns 24hours
  if period == "AM":
    if int(hours) == 12:
      hours = int(hours) - 12
  elif period == "PM":
    if int(hours) >= 1 or int(hours) <= 11:
      hours = int(hours) + 12
  return hours


def convert_24to12_hours(hours): # returns 12hours and period
  if hours == "0":
    hours = int(hours) + 12
    period = "AM"
  elif hours == "12":
    period = "PM"
  elif int(hours) >= 13 and int(hours) <= 23:
    hours = int(hours) - 12
    period = "PM"
  elif int(hours) > 0 and int(hours) < 12:
    period = "AM"
  return hours, period


def find_days_in_hours(hours):
  global __days
  h = int(hours)
  for i in range(int(hours/24)):
    __days += 1
    h = h - 24
  return(__days, str(h))

  
def find_hours_in_minutes(minutes):
  global __hours
  m = int(minutes)
  for i in range(int(m/60)):
    __hours += 1
    m = m - 60
  if m < 10:
    m = '0' + str(m)
  return(__hours, str(m))


def day_to_number(day):
  switcher = {
    "monday": 0,
    "tuesday": 1,
    "wednesday": 2,
    "thursday": 3,
    "friday": 4,
    "saturday": 5,
    "sunday": 6,
  }
  return switcher.get(day, "nothing") 


def num_to_day(num):
  switcher = {
    0: "monday",
    1: "tuesday",
    2: "wednesday",
    3: "thursday",
    4: "friday",
    5: "saturday",
    6: "sunday",
  }
  return switcher.get(num, "nothing") 


def add_time(start, duration, day=""):
  global __days
  global __hours
  
  # split start time
  time, period = start.split()
  _12hours, minutes = time.split(":")

  # split duration
  hours_spent, minutes_spent = duration.split(":")

  # convert period to 24-hour clock
  _24hours = convert_12to24_hours(_12hours, period)

  # add minutes
  added_minutes = int(minutes) + int(minutes_spent)
  new_hours, total_minutes = find_hours_in_minutes(added_minutes)
  #   excess of 60 becomes new_hours

  # add 24hours
  added_hours = int(_24hours) + int(hours_spent) + int(new_hours)
  new_days, total_hours = find_days_in_hours(added_hours)
  #   excess of 24 becomes new_days

  # convert 24-hour clock to 12-hour clock and period
  _12hours, period = convert_24to12_hours(total_hours)

  # increment day by new_days
  if day != "":
    day_num = day_to_number(day.lower())
    day_num += new_days
    while day_num > 6:
      day_num -= 7
    day = num_to_day(day_num).capitalize()

  if new_days == 1 and day == "":
    print("{}:{} {} ({})".format(_12hours, total_minutes, period, "next day"))
    new_time = ("{}:{} {} ({})".format(_12hours, total_minutes, period, "next day"))
  elif new_days == 1 and day != "":
    print("{}:{} {}, {} ({})".format(_12hours, total_minutes, period, day, "next day"))
    new_time = ("{}:{} {}, {} ({})".format(_12hours, total_minutes, period, day, "next day"))
  elif new_days > 1 and day == "":
    print("{}:{} {} ({})".format(_12hours, total_minutes, period, "" + str(new_days) + " days later"))
    new_time = ("{}:{} {} ({})".format(_12hours, total_minutes, period, "" + str(new_days) + " days later"))
  elif new_days > 1 and day != "":
    print("{}:{} {}, {} ({})".format(_12hours, total_minutes, period, day, str(new_days) + " days later"))
    new_time = ("{}:{} {}, {} ({})".format(_12hours, total_minutes, period, day, str(new_days) + " days later"))
  elif day == "":
    print("{}:{} {}".format(_12hours, total_minutes, period))
    new_time = ("{}:{} {}".format(_12hours, total_minutes, period))
  elif day != "":
    print("{}:{} {}, {}".format(_12hours, total_minutes, period, day))
    new_time = ("{}:{} {}, {}".format(_12hours, total_minutes, period, day))
    
  __days = 0
  __hours = 0

  return new_time