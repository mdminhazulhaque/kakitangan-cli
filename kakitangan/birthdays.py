#!/usr/bin/env python3

__author__ = "Md. Minhazul Haque"
__version__ = "0.2.0"
__license__ = "GPLv3"

"""
Copyright (c) 2020 Md. Minhazul Haque
This file is part of mdminhazulhaque/kakitangan-cli
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

import requests
import json
import datetime

def KakitanganBirthdays():
    try:
        headers = KakitanganHeaders.json()
        cookies = KakitanganConfig.load("authorization")
        del cookies["username"]
        year = datetime.datetime.today().strftime("%Y")
        params = (
            ('start', year + '-01-01'),
            ('end', year + '-12-31')
        )
        response = requests.get(KakitanganURLS.BIRTHDAYS, headers=headers, params=params, cookies=cookies)
        content = response.text\
            .replace("'", "\"")\
            .replace("True", "true")\
            .replace("False", "false")
        calendar = {}
        for item in json.loads(content):
            date = item['start']
            name = item['title']
            try:
                calendar[date].append(name)
            except:
                calendar[date] = []
                calendar[date].append(name)
        data = [
            [date, "\n".join(calendar[date])]
            for date in sorted(calendar)
            ]
        return data
    except:
        return False
