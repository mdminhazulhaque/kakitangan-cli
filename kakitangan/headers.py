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

class KakitanganHeaders:
    _default = {
            'authority': 'app.kakitangan.com',
            'cache-control': 'max-age=0',
            'origin': 'https://app.kakitangan.com',
            'upgrade-insecure-requests': '1',
            'user-agent': 'kakitangan-cli/1.0',
            'referer': 'https://app.kakitangan.com/login',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-us,en;q=0.9',
        }
    
    @staticmethod
    def default():
        return _default
    
    @staticmethod
    def urlencoded():
        _urlencoded = {
            'content-type': 'application/x-www-form-urlencoded',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3'
        }
        return {**_urlencoded, **KakitanganHeaders._default}
    
    @staticmethod
    def urlencoded_json():
        _urlencoded_json = {
            'content-type': 'application/x-www-form-urlencoded',
            'accept': 'application/json, text/javascript, */*; q=0.01'
        }
        return {**_urlencoded_json, **KakitanganHeaders._default}
    
    @staticmethod
    def json():
        _json = {
            'content-type': 'application/json',
            'accept': 'application/json, text/javascript, */*; q=0.01'
        }
        return {**_json, **KakitanganHeaders._default}
