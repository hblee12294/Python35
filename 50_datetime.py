# -*- coding: utf-8 -*-

import re
from datetime import datetime, timezone, timedelta

def toTimestamp(dtStr, tzStr):
	tzUTC = timezone(timedelta(hours = int(re.split(r'[\+\-\:]', tzStr)[1])))
	dt = datetime.strptime(dtStr, "%Y-%m-%d %H:%M:%S").replace(tzinfo = tzUTC)
	TS = datetime.fromtimestamp(dt.astimezone(tzUTC))
	return TS

t1 = toTimestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = toTimestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('Pass')
