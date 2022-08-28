from datetime import datetime, date, time


dt = datetime(2011, 10, 29, 20, 30, 21)
print(dt)

print(dt.date())

new_time = dt.strftime('%d.%m.%Y %H:%M')
print(new_time)

dt2 = datetime(2011, 11, 15, 22, 30)

delta = dt2 - dt
print(delta)
print(type(delta))



