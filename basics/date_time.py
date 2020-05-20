from datetime import datetime, timedelta, timezone, timedelta
import dateutil.parser

"""Parsing a string into a timezone aware datetime object"""

dt = datetime.datetime.strptime("2020-04-30T14:07:00-0500", "%Y-%m-%dT%H:%M:%S%z")
print(dt)
# or
dt = dateutil.parser.parse("2020-04-30T14:07:00-0500")
print(dt)

datetime.datetime(2020, 4, 30, 14, 07, 00, tzinfo=tzoffset(None, -18000))


"""Constructing timezone-aware datetimes"""

JST = timezone(timedelta(hours=+9))
dt = datetime(2015, 1, 1, 12, 0, 0, tzinfo=JST)
print(dt)
print(dt.tzname())

dt = datetime(2015, 1, 1, 12, 0, 0, tzinfo=timezone(timedelta(hours=9), 'JST'))
print(dt.tzname)


"""Computing time differences"""

now = datetime.now()
then = datetime(2016, 5, 23)

delta = now - then
print(delta.days)
print(delta.seconds)


"""Basic datetime objects usage"""

# Date object
today = datetime.date.today()
new_year = datetime.date(2017, 1, 1)

# Time object
noon = datetime.time(12, 0, 0)

# Current datetime
now = datetime.datetime.now()

# Datetime object
millenium_turn = datetime.datetime(2000, 1, 1, 0, 0, 0)


"""Simple date arithmetic PAG.69"""

