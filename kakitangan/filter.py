#!/usr/bin/env python3

__author__ = "Md. Minhazul Haque"
__version__ = "0.1.0"
__license__ = "GPLv3"

"""
Copyright (c) 2018 Md. Minhazul Haque
This file is part of mdminhazulhaque/bd-mrp-api
(see https://github.com/mdminhazulhaque/banglalionwimaxapi).
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
"""

from .const import KakitanganConst
from .config import KakitanganConfig
import datetime

FMT = "%Y-%m-%d"
START = "start"
END = "end"
TITLE = "title"
HOVER = "hover"
FULL_DAY = "full_day"
LEAVE_TYPE = "leave_type"

class KakitanganFilter:
    @staticmethod
    def _daterange(start, end):
        for n in range(int ((end - start).days)):
            yield start + datetime.timedelta(n)

    @staticmethod
    def _extract_calendar(raw, myleave=False, colleagues=False):
        calendar = {}
        for item in raw:
            start = datetime.datetime.strptime(item[START], FMT)
            end = datetime.datetime.strptime(item[END], FMT)
            for dateobj in KakitanganFilter._daterange(start, end):
                date = dateobj.strftime(FMT)
                if myleave and (item[HOVER][FULL_DAY] in ["(AM)", "(PM)"]):
                    item[TITLE] = item[TITLE] + " " + item[HOVER][FULL_DAY]
                if colleagues:
                    #print(item[TITLE] + " " + item[HOVER][LEAVE_TYPE])
                    if "(" not in item[TITLE]:
                        item[TITLE] = item[TITLE] + " (" + item[HOVER][LEAVE_TYPE] + ")"
                try:
                    calendar[date].append(item[TITLE])
                except:
                    calendar[date] = []
                    calendar[date].append(item[TITLE])   
        return calendar

    @staticmethod
    def filter_calendar(calendartype, all=False, today=False, since=False,
                        untill=False, custom=False):
        raw = KakitanganConfig.load(calendartype)
        if raw == False:
            print("Calendar not updated")
            return
        
        myleave, colleagues = False, False
        if calendartype == KakitanganConst.CALENDAR:
            myleave = True
        elif calendartype == KakitanganConst.COLLEAGUES:
            colleagues = True
        calendar = KakitanganFilter._extract_calendar(raw, myleave, colleagues)
        
        today_date = datetime.datetime.now()        
        untill_date = datetime.datetime.strptime(untill, FMT) if untill else None
        since_date = datetime.datetime.strptime(since, FMT) if since else None
        custom_date = datetime.datetime.strptime(custom, FMT) if custom else None
        
        data = []
        
        for date in sorted(calendar):
            entry = [date, "\n".join(calendar[date])]
            this_date = datetime.datetime.strptime(date, FMT)
            
            if since and since_date > this_date:
                continue
                
            if not all and today_date > this_date:
                continue
            
            if today and (today_date - this_date).days == 0:
                return [entry]
                break
            
            if custom and (this_date - custom_date).days == 0:
                return [entry]
                break
            
            if not today:
                data.append(entry)
                            
            if untill and this_date >= untill_date:
                break
        return data
