import pytz
from datetime import datetime


def time_to_seconds(hour, minute, second):
    return hour * 3600 + minute * 60 + second


time_zones = pytz.all_timezones
time = input().split(':')
seconds = time_to_seconds(int(time[0]), int(time[1]), int(time[2]))
minimum = 24 * 3600
min_time_zone = ''

for time_zone in time_zones:
    time_zone_time = datetime.now(pytz.timezone(time_zone)).time()
    if abs(seconds - time_to_seconds(time_zone_time.hour, time_zone_time.minute, time_zone_time.second)) < minimum:
        min_time_zone = time_zone
        minimum = abs(seconds - time_to_seconds(time_zone_time.hour, time_zone_time.minute, time_zone_time.second))

print(min_time_zone)
