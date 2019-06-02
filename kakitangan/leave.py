#!/usr/bin/env python3

__author__ = "Md. Minhazul Haque"
__version__ = "0.2.0"
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

from .urls import KakitanganURLS
from .headers import KakitanganHeaders
from .config import KakitanganConfig
from .filter import KakitanganFilter
from .const import KakitanganConst

import requests
import json

class KakitanganLeave():
    @staticmethod
    def myleavestat():
        cookies = KakitanganConfig.load("authorization")
        headers = KakitanganHeaders.json()
        headers['authorization'] = 'Token ' + cookies['ATK']
        response = requests.get(KakitanganURLS.LEAVE_POLICY + cookies['username'],
                                headers=headers)
        
        data = []
        for item in response.json():
            total = item["days"]
            avail = item["available_days"]
            used = item["used_days"]
            data.append([
                item["name"],
                "{0:g}/{1:g} ({2:g} used)".format(avail, total, used)
                .replace("(0 used)", "")
            ])
        return data
    
    @staticmethod
    def loadleaves():
        cookies = KakitanganConfig.load("authorization")
        del cookies["username"]
        saved = 0
        calendartypes = [
            KakitanganConst.HOLIDAY_EVENT,
            KakitanganConst.COLLEAGUES,
            KakitanganConst.CALENDAR
        ]
        for calendartype in calendartypes:
            data = {
                'action': calendartype,
                'employee': '',
                'csrfmiddlewaretoken': cookies['csrftoken'],
                'start': '2019-04-28',
                'end': '2019-06-09'
            }
            response = requests.post('https://app.kakitangan.com/leave/leave/calendar',
                                     headers=KakitanganHeaders.urlencoded_json(),
                                     cookies=cookies,
                                     data=data)
            
            if response.status_code == 200:
                KakitanganConfig.save(response.json(), calendartype)
                saved += 1
        if saved == len(calendartypes):
            return True
        else:
            return False
