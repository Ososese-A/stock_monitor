from datetime import date, datetime, time

now = datetime.now()
print("Current date and time is:")
print(now.strftime("%y-%m-%d %H:%M:%S %p"))


from datetime import date

today = date.today()
print("today is:", today)
print("day:", today.day)
print("month:", today.month)
print("year:", today.year)

print(today.strftime("%A, %dth %B %Y"))

print(today.strftime("%a, %dth %b %y"))

next_year = today.replace(year = today.year +1)

print(next_year)

NikolaTesla = date(1856, 7, 10)
print (NikolaTesla)
Teals = date.fromisoformat("1856-07-10")
print(Teals)

difference = abs(next_year - today)

print(f"only {difference.days} days until next year")

print(NikolaTesla.weekday())

now = datetime.now()

print("right now it's:", now)

print("it's the {}th minute of the {}nd hour, of the {}th day of the {}nd month".format(now.minute, now.hour, now.day, now.month))

chernobyl = datetime.fromisoformat("1986-04-26 01:23:40:000+04:00")

print(chernobyl)

print(chernobyl.strftime("%A %B %dth, %Y at %X MSD(%Z)"))

print("MSD is actually:", chernobyl.tzinfo)

my_time = time(15, 33, 8)

time.fromisoformat("15:33:08-07:00")

print(my_time)

print(my_time.strftime("%I:%M %p"))

my_date = date(2022, 5, 22)
my_bday = datetime.combine(my_date, my_time)

print(my_bday)
