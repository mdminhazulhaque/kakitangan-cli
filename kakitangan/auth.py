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
from .const import KakitanganConst

import requests

def KakitanganAuth(username, password):
    session = requests.Session()
    response = session.get(KakitanganURLS.LOGIN)
    csrfmiddlewaretoken = session.cookies.get_dict()['csrftoken']
    data = {
        'username': username,
        'password': password,
        'next': '/redirect',
        'csrfmiddlewaretoken': csrfmiddlewaretoken
    }
    response = session.post(KakitanganURLS.LOGIN,
                            data=data,
                            headers=KakitanganHeaders.urlencoded())
    
    cookies = session.cookies.get_dict()
    
    if 'sessionid' not in cookies:
        return False
    
    data = {
        'username': username,
        'password': password,
    }
    response = session.post(KakitanganURLS.AUTH_TOKEN,
                            json=data,
                            headers=KakitanganHeaders.json())
    
    if 'token' not in response.json():            
        return False
    
    cookies = session.cookies.get_dict()            
    config = {
        'sessionid': cookies['sessionid'],
        'csrftoken': cookies['csrftoken'],
        'username': data['username'],
        'ATK': response.json()['token']
    }
    
    success = KakitanganConfig.save(config, name=KakitanganConst.AUTHORIZATION)
    return success
