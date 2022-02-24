# _*_coding:UTF-8 _*_
'''
使用 time 模块展示当前日期和时间
将天、小时、分钟转换为秒
使用 Pandas 获取当前日期和时间
将字符串转换为日期时间对象
以毫秒为单位获取当前时间
以 MST、EST、UTC、GMT 和 HST 获取当前日期时间
从给定的日期当中获取星期几
计算两个日期时间对象之间的时差
将 5 分钟添加到 Unix 时间戳
在 Python 中遍历一系列日期
巴黎时间更改为纽约时间
使用 Python 获得最后7个工作日
从今天的日期和一个人的生日推算年龄
获得本月的第一个星期二
将整数转换为日期对象
当前日期减去 N 天的天数
比较两个日期
从 datetime 对象中提取年份
在 Python 中找到星期几
从当前日期获取 7 天前的日期
将两个日期时间对象之间的差值转换为秒
获得任何一个月的第三个星期五
从 Python 中的周数获取日期
获取特定日期的工作日
创建一个 15 分钟前的 DateTime
从特定日期获取周的开始和结束日期
两个日期之间的差异（以秒为单位）
以这种格式获取昨天的日期MMDDYY
从今天的日期获取上周三
所有可用时区的列表打印
获取指定开始日期和结束日期之间的日期范围
毫秒转换为数据
查找给定日期之后的第一个星期日的日期
将（Unix）时间戳秒转换为日期和时间字符串
以月为单位的两个日期之间的差异
将本地时间字符串转换为 UTC
获取当月的最后一个星期四
从特定日期查找一年中的第几周
从给定日期获取星期几
用 AM PM 打印当前时间
获得一个月的最后一天
从工作日值中获取工作日名称
将 N 小时数添加到当前日期时间
从当前日期获取年、月、日、小时、分钟
获取特定月份和年份的最后一个星期日
查找特定日期的年份中的哪一天
查找当前日期是工作日还是周末
组合 datetime.date 和 datetime.time 对象
获得每月的第 5 个星期一
将日期时间对象转换为日期对象
获取没有微秒的当前日期时间
将 N 秒数添加到特定日期时间
从当前日期获取两位数的月份和日期
从特定日期获取月份数据的开始和结束日期
以周为单位的两个日期之间的差异
将字符串格式的日期转换为 Unix 时间戳
获取最后一个周日和周六的日期
检查对象是否属于 datetime.date 类型
获取特定日期的周数
获取 UTC 时间
获取本周的开始和结束日期
两个日期之间的差异（以分钟为单位）
将日期时间对象转换为日期字符串
获得上周五
将 3 周添加到任何特定日期
在其他两个日期之间生成一个随机日期
查找从今天开始的第一个星期一的日期
两个日期之间的差异（以天为单位）
向当前日期添加六个月
将数据时间对象转换为 Unix（时间戳）
将年、月、日、时、分、秒的 N 个数字添加到当前日期时间
获取指定开始日期和结束日期之间的日期范围
减去 N 个年、月、日、时、分、秒到当前日期时间
获取指定年份和月份的月份第一天的工作日和月份的天数
打印特定年份的所有星期一
打印特定年份的日历
从月份编号中获取月份名称
从给定日期获取一周的开始和结束日期
根据当前日期查找上一个和下一个星期一的日期
获取当前季度的第一个日期和最后一个日期
'''
# 使用time模块展示当前日期和时间
import time
from time import gmtime, strftime

t = time.localtime()
print(time.asctime(t))
print(strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))
print(strftime("%A", gmtime()))
print(strftime("%D", gmtime()))
print(strftime("%B", gmtime()))
print(strftime("%y", gmtime()))

# Convert seconds into GMT date
print(strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime(1234567890)))

# 将天、小时、分钟转换为秒
SECONDS_PER_MINUTE = 60
SECONDS_PER_HOUR = 3600
SECONDS_PER_DAY = 86400

# Read the inputs from user
days = int(input("Enter number of Days: "))
hours = int(input("Enter number of Hours: "))
minutes = int(input("Enter number of Minutes: "))
seconds = int(input("Enter number of Seconds: "))

# Calculate the days, hours, minutes and seconds
total_seconds = days * SECONDS_PER_DAY
total_seconds = total_seconds + (hours * SECONDS_PER_HOUR)
total_seconds = total_seconds + (minutes * SECONDS_PER_MINUTE)
total_seconds = total_seconds + seconds

# Display the result
print("Total number of seconds: ", "%d" % (total_seconds))
# 使用Pandas获取当前日期和时间
import pandas as pd

print(pd.datetime.now())
print(pd.datetime.now().date())
print(pd.datetime.now().year)
print(pd.datetime.now().month)
print(pd.datetime.now().day)
print(pd.datetime.now().hour)
print(pd.datetime.now().minute)
print(pd.datetime.now().second)
print(pd.datetime.now().microsecond)
# 将字符串转换为日期时间对象
from datetime import datetime
from dateutil import parser

d1 = "Jan 7 2015  1:15PM"
d2 = "2015 Jan 7  1:33PM"

# If you know date format
date1 = datetime.strptime(d1, '%b %d %Y %I:%M%p')
print(type(date1))
print(date1)

# If you don't know date format
date2 = parser.parse(d2)
print(type(date2))
print(date2)

# 以毫秒为单位获取当前时间
import time

milliseconds = int(round(time.time() * 1000))
print(milliseconds)

# 以MST、EST、UTC、GMT和HST获取当前日期时间
from datetime import datetime
from pytz import timezone

mst = timezone('MST')
print("Time in MST:", datetime.now(mst))
est = timezone('EST')
print("Time in EST:", datetime.now(est))
utc = timezone('UTC')
print("Time in UTC:", datetime.now(utc))
gmt = timezone('GMT')
print("Time in GMT:", datetime.now(gmt))
hst = timezone('HST')
print("Time in HST:", datetime.now(hst))
# 7从给定的日期当中获取星期几
import datetime

dayofweek = datetime.date(2010, 6, 16).strftime("%A")
print(dayofweek)
# weekday Monday is 0 and Sunday is 6
print("weekday():", datetime.date(2010, 6, 16).weekday())

# isoweekday() Monday is 1 and Sunday is 7
print("isoweekday()", datetime.date(2010, 6, 16).isoweekday())

dayofweek = datetime.datetime.today().strftime("%A")
print(dayofweek)
print("weekday():", datetime.datetime.today().weekday())
print("isoweekday()", datetime.datetime.today().isoweekday())
# 8计算两个日期时间对象之间的时差
import datetime
from datetime import timedelta

datetimeFormat = '%Y-%m-%d %H:%M:%S.%f'
date1 = '2016-04-16 10:01:28.585'
date2 = '2016-03-10 09:56:28.067'
diff = datetime.datetime.strptime(date1, datetimeFormat) \
       - datetime.datetime.strptime(date2, datetimeFormat)

print("Difference:", diff)
print("Days:", diff.days)
print("Microseconds:", diff.microseconds)
print("Seconds:", diff.seconds)
# 将5分钟添加到Unix时间戳
import datetime
import calendar

future = datetime.datetime.utcnow() + datetime.timedelta(minutes=5)
print(calendar.timegm(future.timetuple()))
# 10在Python中遍历一系列日期
import datetime

start = datetime.datetime.strptime("21-06-2020", "%d-%m-%Y")
end = datetime.datetime.strptime("05-07-2020", "%d-%m-%Y")
date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end - start).days)]

for date in date_generated:
    print(date.strftime("%d-%m-%Y"))
# 11巴黎时间更改为纽约时间
import pendulum

in_paris = pendulum.datetime(2016, 8, 7, 22, 24, 30, tz='Europe/Paris')
print(in_paris)

in_us = in_paris.in_timezone('America/New_York')
print(in_us)
# 12使用Python获得最后7个工作日
from datetime import date
from datetime import timedelta

today = date.today()

for i in range(7):
    d = today - timedelta(days=i)
    if d.weekday() < 5:
        print(d)
# 13从今天的日期和一个人的生日推算年龄
from datetime import date


def calculate_age(born):
    today = date.today()
    try:
        birthday = born.replace(year=today.year)
    except ValueError:
        birthday = born.replace(year=today.year, month=born.month + 1, day=1)
    if birthday > today:
        return today.year - born.year - 1
    else:
        return today.year - born.year


print(calculate_age(date(2001, 3, 1)))
# 14获得本月的第一个星期二
import calendar
from datetime import datetime

c = calendar.Calendar(firstweekday=calendar.SUNDAY)
monthcal = c.monthdatescalendar(datetime.today().year, datetime.today().month)

try:
    tues = [day for week in monthcal for day in week if
            day.weekday() == calendar.TUESDAY and day.month == datetime.today().month][0]
    print(tues)
except IndexError:
    print('No date found')
# 15将整数转换为日期对象
from datetime import datetime

i = 1545730073
timestamp = datetime.fromtimestamp(i)

print(timestamp)
print(type(timestamp))
# 16当前日期减去N天的天数
from datetime import datetime, timedelta

d = datetime.today() - timedelta(days=5)
print(d)
# 17比较两个日期
import datetime

a = datetime.datetime(2020, 12, 31, 23, 59, 59)
b = datetime.datetime(2020, 11, 30, 23, 59, 59)

print(a < b)
print(a > b)
# 18从datetime对象中提取年份
import datetime

year = datetime.date.today().year
print(year)
# 19在Python中找到星期几
import pendulum

dt = pendulum.parse('2021-05-18')
print(dt.day_of_week)

dt = pendulum.parse('2021-05-01')
print(dt.day_of_week)

dt = pendulum.parse('2021-05-21')
print(dt.day_of_week)
# 20从当前日期获取7天前的日期
from datetime import datetime, timedelta

now = datetime.now()

for x in range(7):
    d = now - timedelta(days=x)
    print(d.strftime("%Y-%m-%d"))
# 21将两个日期时间对象之间的差值转换为秒
import datetime

time1 = datetime.datetime.strptime('19 01 2021', '%d %m %Y')
time2 = datetime.datetime.strptime('25 01 2021', '%d %m %Y')

difference = time2 - time1
print(difference)

seconds = difference.total_seconds()
print(seconds)
# 22获得任何一个月的第三个星期五
import calendar

c = calendar.Calendar(firstweekday=calendar.SUNDAY)
year = 2021
month = 5
monthcal = c.monthdatescalendar(year, month)

try:
    third_friday = [day for week in monthcal for day in week if
                    day.weekday() == calendar.FRIDAY and day.month == month][2]
    print(third_friday)
except IndexError:
    print('No date found')
# 23从Python中的周数获取日期
import datetime
from dateutil.relativedelta import relativedelta

week = 25
year = 2021
date = datetime.date(year, 1, 1) + relativedelta(weeks=+week)
print(date)
# 24获取特定日期的工作日
import datetime

print(datetime.date(2020, 5, 15).isocalendar()[2])
# 25创建一个 15分钟前的DateTime
import datetime

dt = datetime.datetime.now() - datetime.timedelta(minutes=15)
print(dt)
# 26从特定日期获取周的开始和结束日期
import pendulum

dt = pendulum.datetime(2012, 9, 5)

start = dt.start_of('week')
print(start.to_datetime_string())

end = dt.end_of('week')
print(end.to_datetime_string())
# 27两个日期之间的差异（以秒为单位）
from datetime import datetime

fmt = '%Y-%m-%d %H:%M:%S'
d1 = datetime.strptime('2020-01-01 17:31:22', fmt)
d2 = datetime.strptime('2020-01-03 17:31:22', fmt)

days_diff = d2 - d1
print(days_diff.days * 24 * 60 * 60)
# 28以这种格式获取昨天的日期MMDDYY
from datetime import date, timedelta

yesterday = date.today() - timedelta(days=1)
print(yesterday.strftime('%m%d%y'))
# 29从今天的日期获取上周三
from datetime import date
from datetime import timedelta

today = date.today()

offset = (today.weekday() - 2) % 7
wednesday = today - timedelta(days=offset)
print(wednesday)
# 30所有可用时区的列表打印
import pytz

for i in pytz.all_timezones:
    print(i)
# 31获取指定开始日期和结束日期之间的日期范围
import datetime

start = datetime.datetime.strptime("21-06-2020", "%d-%m-%Y")
end = datetime.datetime.strptime("05-07-2020", "%d-%m-%Y")
date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end - start).days)]

for date in date_generated:
    print(date.strftime("%d-%m-%Y"))
# 32毫秒转换为数据
import datetime

time_in_millis = 1596542285000
dt = datetime.datetime.fromtimestamp(time_in_millis / 1000.0, tz=datetime.timezone.utc)
print(dt)
# 33查找给定日期之后的第一个星期日的日期
import datetime


def next_weekday(d, weekday):
    days_ahead = weekday - d.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    return d + datetime.timedelta(days_ahead)


d = datetime.date(2021, 5, 16)
next_sunday = next_weekday(d, 6)
print(next_sunday)
# 34将（Unix）时间戳秒转换为日期和时间字符串
from datetime import datetime

dateStr = datetime.fromtimestamp(1415419007).strftime("%A, %B %d, %Y %I:%M:%S")
print(type(dateStr))
print(dateStr)
# 35以月为单位的两个日期之间的差异
from datetime import datetime
from dateutil import relativedelta

date1 = datetime.strptime('2014-01-12 12:00:00', '%Y-%m-%d %H:%M:%S')
date2 = datetime.strptime('2021-07-15 12:00:00', '%Y-%m-%d %H:%M:%S')

r = relativedelta.relativedelta(date2, date1)
print(r.months + (12 * r.years))
# 36将本地时间字符串转换为UTC
from datetime import *
from dateutil import *
from dateutil.tz import *

utc_zone = tz.gettz('UTC')
local_zone = tz.gettz('America/Chicago')

utc_zone = tz.tzutc()
local_zone = tz.tzlocal()

local_time = datetime.strptime("2020-10-25 15:12:00", '%Y-%m-%d %H:%M:%S')
print(local_time)
local_time = local_time.replace(tzinfo=local_zone)
print(local_time)

utc_time = local_time.astimezone(utc_zone)
print(utc_time)

utc_string = utc_time.strftime('%Y-%m-%d %H:%M:%S')
print(utc_string)
# 37获取当月的最后一个星期四
import calendar
from datetime import datetime

month = calendar.monthcalendar(datetime.today().year, datetime.today().month)

thrusday = max(month[-1][calendar.THURSDAY], month[-2][calendar.THURSDAY])
print(thrusday)
# 38从特定日期查找一年中的第几周
import pendulum

dt = pendulum.parse('2015-05-18')
print(dt.week_of_year)

dt = pendulum.parse('2019-12-01')
print(dt.week_of_year)

dt = pendulum.parse('2018-01-21')
print(dt.week_of_year)
# 39从给定日期获取星期几
import datetime
import calendar

dt = datetime.datetime(2021, 4, 25, 23, 24, 55, 173504)
print(calendar.day_name[dt.weekday()])
# 40用AMPM打印当前时间
from datetime import datetime

print(datetime.today().strftime("%I:%M %p"))

# 41获得一个月的最后一天
import calendar

print(calendar.monthrange(2002, 1)[1])
print(calendar.monthrange(2008, 6)[1])
print(calendar.monthrange(2012, 2)[1])
print(calendar.monthrange(2015, 2)[1])
# 42从工作日值中获取工作日名称
import calendar

print(calendar.day_name[0])
print(calendar.day_name[1])
print(calendar.day_name[2])
print(calendar.day_name[3])
print(calendar.day_name[4])
print(calendar.day_name[5])
print(calendar.day_name[6])
# 43将N小时数添加到当前日期时间
from datetime import datetime, timedelta

d = datetime.today() + timedelta(hours=18)
print(d)
# 44从当前日期获取年、月、日、小时、分钟
import datetime

now = datetime.datetime.now()
print(now.year, now.month, now.day, now.hour, now.minute, now.second)
# 45获取特定月份和年份的最后一个星期日
import calendar

month = calendar.monthcalendar(2021, 2)

last_sunday = max(month[-1][calendar.SUNDAY], month[-2][calendar.SUNDAY])
print(last_sunday)

# 46查找特定日期的年份中的哪一天
import pendulum

dt = pendulum.parse('2015-05-18')
print(dt.day_of_year)

dt = pendulum.parse('2019-12-01')
print(dt.day_of_year)

dt = pendulum.parse('2018-01-21')
print(dt.day_of_year)

# 47查找当前日期是工作日还是周末
import datetime

weekno = datetime.datetime.today().weekday()
if weekno < 5:
    print("Weekday")
else:  # 5 Sat, 6 Sun
    print("Weekend")
# 48组合datetime.date和datetime.time对象
import datetime

d = datetime.datetime.combine(datetime.date(2020, 11, 14),
                              datetime.time(10, 23, 15))

print(d)

# 49获得每月的第5个星期一
import calendar

c = calendar.Calendar(firstweekday=calendar.SUNDAY)
year = 2016
month = 2
monthcal = c.monthdatescalendar(year, month)

try:
    fifth_monday = [day for week in monthcal for day in week if
                    day.weekday() == calendar.MONDAY and day.month == month][4]
    print(fifth_monday)
except IndexError:
    print('No date found')

# 50将日期时间对象转换为日期对象
from datetime import datetime

datetime_obj = datetime(2020, 12, 15, 10, 15, 45, 321474)
print(datetime_obj)

date_obj = datetime_obj.date()
print(date_obj)

# 51获取没有微秒的当前日期时间
from datetime import datetime

print(datetime.now().isoformat(' ', 'seconds'))

# 52将N秒数添加到特定日期时间
import datetime

a = datetime.datetime(2020, 12, 31, 23, 59, 45)
b = a + datetime.timedelta(seconds=30)

print(a)
print(b)

# 53从当前日期获取两位数的月份和日期
import datetime

dt = datetime.datetime.now()

print(dt.strftime('%m'))
print('{:02d}'.format(dt.month))
print(f'{dt.month:02d}')
print('%02d' % dt.month)

print(dt.strftime('%d'))
print('{:02d}'.format(dt.day))
print(f'{dt.day:02d}')
print('%02d' % dt.day)

# 54从特定日期获取月份数据的开始和结束日期
import pendulum

dt = pendulum.datetime(2012, 9, 5)

start = dt.start_of('month')
print(start.to_datetime_string())

end = dt.end_of('month')
print(end.to_datetime_string())

# 55以周为单位的两个日期之间的差异
from datetime import date

date1 = date(2020, 12, 23)
date2 = date(2021, 5, 11)

days = abs(date1 - date2).days
print(days // 7)

# 56将字符串格式的日期转换为Unix时间戳
import datetime

stime = '15/05/2021'
print(datetime.datetime.strptime(stime, "%d/%m/%Y").timestamp())

# 57获取最后一个周日和周六的日期
from datetime import datetime, timedelta


def prior_week_end():
    return datetime.now() - timedelta(days=((datetime.now().isoweekday() + 1) % 7))


def prior_week_start():
    return prior_week_end() - timedelta(days=6)


print('Sunday', format(prior_week_start()))
print('Saturday', format(prior_week_end()))

# 58检查对象是否属于datetime.date类型
import datetime

x = '2012-9-1'
y = datetime.date(2012, 9, 1)

print(isinstance(x, datetime.date))
print(isinstance(y, datetime.date))

# 59获取特定日期的周数
import datetime

print(datetime.date(2020, 5, 15).isocalendar()[1])

# 60获取UTC时间
from datetime import datetime

dt = datetime.utcnow()
print(dt)

# 61获取本周的开始和结束日期
import pendulum

today = pendulum.now()

start = today.start_of('week')
print(start.to_datetime_string())

end = today.end_of('week')
print(end.to_datetime_string())

# 62两个日期之间的差异（以分钟为单位）
from datetime import datetime

fmt = '%Y-%m-%d %H:%M:%S'
d1 = datetime.strptime('2010-01-01 17:31:22', fmt)
d2 = datetime.strptime('2010-01-03 17:31:22', fmt)

days_diff = d2 - d1
print(days_diff.days * 24 * 60)

# 63将日期时间对象转换为日期字符串
import datetime

t = datetime.datetime(2020, 12, 23)
x = t.strftime('%m/%d/%Y')
print(x)

# 64获得上周五
from datetime import date
from datetime import timedelta

today = date.today()

offset = (today.weekday() - 4) % 7
friday = today - timedelta(days=offset)
print(friday)

# 65将3周添加到任何特定日期
import pendulum

dt = pendulum.datetime(2012, 2, 15)
dt = dt.add(weeks=3)
print(dt.to_date_string())

# 66 在其他两个日期之间生成一个随机日期
import random
import time


def str_time_prop(start, end, time_format, prop):
    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))
    ptime = stime + prop * (etime - stime)
    return time.strftime(time_format, time.localtime(ptime))


def random_date(start, end, prop):
    return str_time_prop(start, end, '%m/%d/%Y %I:%M %p', prop)


print(random_date("1/1/2020 1:10 PM", "1/1/2021 1:10 AM", random.random()))

# 67查找从今天开始的第一个星期一的日期
from dateutil.rrule import rrule, WEEKLY, MO
from datetime import date

next_monday = rrule(freq=WEEKLY, dtstart=date.today(), byweekday=MO, count=1)[0]
print(next_monday)

# 68两个日期之间的差异（以天为单位）
from datetime import date

d1 = date(2019, 8, 18)
d2 = date(2021, 12, 10)

days_diff = d2 - d1
print(days_diff.days)

# 69向当前日期添加六个月
from datetime import datetime
from dateutil.relativedelta import *

date = datetime.now()
print(date)

date = date + relativedelta(months=+6)
print(date)

# 70将数据时间对象转换为Unix（时间戳）
import datetime
import time

# Saturday, October 10, 2015 10:10:00 AM
date_obj = datetime.datetime(2015, 10, 10, 10, 10)
print("Unix Timestamp: ", (time.mktime(date_obj.timetuple())))
# 71将年、月、日、时、分、秒的N个数字添加到当前日期时间
import datetime
from dateutil.relativedelta import relativedelta

add_days = datetime.datetime.today() + relativedelta(days=+6)
add_months = datetime.datetime.today() + relativedelta(months=+6)
add_years = datetime.datetime.today() + relativedelta(years=+6)

add_hours = datetime.datetime.today() + relativedelta(hours=+6)
add_mins = datetime.datetime.today() + relativedelta(minutes=+6)
add_seconds = datetime.datetime.today() + relativedelta(seconds=+6)

print("Current Date Time:", datetime.datetime.today())
print("Add 6 days:", add_days)
print("Add 6 months:", add_months)
print("Add 6 years:", add_years)
print("Add 6 hours:", add_hours)
print("Add 6 mins:", add_mins)
print("Add 6 seconds:", add_seconds)

# 获取指定开始日期和结束日期之间的日期范围
import datetime

start = datetime.datetime.strptime("2016-06-15", "%Y-%m-%d")
end = datetime.datetime.strptime("2016-06-30", "%Y-%m-%d")
date_array = \
    (start + datetime.timedelta(days=x) for x in range(0, (end - start).days))

for date_object in date_array:
    print(date_object.strftime("%Y-%m-%d"))

# 个年、月、日、时、分、秒到当前日期时间
import datetime
from dateutil.relativedelta import relativedelta

sub_days = datetime.datetime.today() + relativedelta(days=-6)
sub_months = datetime.datetime.today() + relativedelta(months=-6)
sub_years = datetime.datetime.today() + relativedelta(years=-6)

sub_hours = datetime.datetime.today() + relativedelta(hours=-6)
sub_mins = datetime.datetime.today() + relativedelta(minutes=-6)
sub_seconds = datetime.datetime.today() + relativedelta(seconds=-6)

print("Current Date Time:", datetime.datetime.today())
print("Subtract 6 days:", add_days)
print("Subtract 6 months:", add_months)
print("Subtract 6 years:", add_years)
print("Subtract 6 hours:", add_hours)
print("Subtract 6 mins:", add_mins)
print("Subtract 6 seconds:", add_seconds)

# 获取指定年份和月份的月份第一天的工作日和月份的天数
import calendar

print("Year:2002 - Month:2")
month_range = calendar.monthrange(2002, 2)
print("Weekday of first day of the month:", month_range[0])
print("Number of days in month:", month_range[1])
print()
print("Year:2010 - Month:5")
month_range = calendar.monthrange(2010, 5)
print("Weekday of first day of the month:", month_range[0])
print("Number of days in month:", month_range[1])

# 打印特定年份的所有星期一
from datetime import date, timedelta

year = 2018
date_object = date(year, 1, 1)
date_object += timedelta(days=1 - date_object.isoweekday())

while date_object.year == year:
    print(date_object)
    date_object += timedelta(days=7)

# 打印特定年份的日历
import calendar

cal_display = calendar.TextCalendar(calendar.MONDAY)
# Year: 2019
# Column width: 1
# Lines per week: 1
# Number of spaces between month columns: 0
# No. of months per column: 2
print(cal_display.formatyear(2019, 1, 1, 0, 2))

# 从月份编号中获取月份名称
import calendar
import datetime

# Month name from number
print("Month name from number 5:")
month_num = 1
month_abre = datetime.date(2015, month_num, 1).strftime('%b')
month_name = datetime.date(2015, month_num, 1).strftime('%B')
print("Short Name:", month_abre)
print("Full  Name:", month_name)

print("\nList of all months from calendar")
# Print list of all months from calendar
for month_val in range(1, 13):
    print(calendar.month_abbr[month_val], "-", calendar.month_name[month_val])

# 从给定日期获取一周的开始和结束日期
from datetime import datetime, timedelta

date_str = '2018-01-14'
date_obj = datetime.strptime(date_str, '%Y-%m-%d')

start_of_week = date_obj - timedelta(days=date_obj.weekday())  # Monday
end_of_week = start_of_week + timedelta(days=6)  # Sunday
print(start_of_week)
print(end_of_week)

# 根据当前日期查找上一个和下一个星期一的日期
import datetime

today = datetime.date.today()
last_monday = today - datetime.timedelta(days=today.weekday())
coming_monday = today + datetime.timedelta(days=-today.weekday(), weeks=1)
print("Today:", today)
print("Last Monday:", last_monday)
print("Coming Monday:", coming_monday)

# 获取当前季度的第一个日期和最后一个日期
from datetime import datetime, timedelta

current_date = datetime.now()
current_quarter = round((current_date.month - 1) / 3 + 1)
first_date = datetime(current_date.year, 3 * current_quarter - 2, 1)
last_date = datetime(current_date.year, 3 * current_quarter + 1, 1) \
            + timedelta(days=-1)

print("First Day of Quarter:", first_date)
print("Last Day of Quarter:", last_date)
