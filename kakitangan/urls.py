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

class KakitanganURLS:
    LOGIN = 'https://app.kakitangan.com/login'
    AUTH_TOKEN = 'https://app.kakitangan.com/api/v1/get_auth_token'
    ME = 'https://app.kakitangan.com/api/v1/user/me'
    LEAVE_POLICY = 'https://app.kakitangan.com/api/v1/leave/policy/'
    USER = 'https://app.kakitangan.com/api/v1/user/'
    CLAIMS = 'https://app.kakitangan.com/claims/'
    CLAIMS_SETTINGS = 'https://app.kakitangan.com/api/v1/claims/settings/subscribed'
    CALENDAR = 'https://app.kakitangan.com/leave/leave/calendar'
    BIRTHDAYS = 'https://app.kakitangan.com/benefits/birthdays.json'
