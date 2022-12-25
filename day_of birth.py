import datetime
import calendar

date_of_birth = input("Podaje date urodziń w formacie dzień-miesiąc-rok (np. 1-1-2000): ")
day, month, year = date_of_birth.split("-")  # (1, 1, 2000)

date_of_birth = datetime.datetime(int(year), int(month), int(day))

day_name = calendar.day_name[date_of_birth.weekday()]
print(day_name)
