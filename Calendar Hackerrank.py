import calendar
Weekday = {'0' : 'MONDAY','1' : 'TUESDAY', '2' : 'WEDNESDAY', '3' : 'THURSDAY','4' : 'FRIDAY','5' : 'SATURDAY', '6' : 'SUNDAY'}
date=input()
calendar_date=list(map(int, date.split()))
print(Weekday[str(calendar.weekday(calendar_date[2], calendar_date[0], calendar_date[1]))])


