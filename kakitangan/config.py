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

from appdirs import user_config_dir
from .const import KakitanganConst
import json
import os

BASE = user_config_dir("kakitangan-cli") + os.sep
JSON = ".json"

class KakitanganConfig:    
    @staticmethod
    def load(name):
        try:
            target = BASE + name + JSON
            with open(target, "r") as fp:
                data = json.load(fp)
            return data
        except:
            return False
    
    @staticmethod
    def save(data, name):
        if not os.path.exists(BASE):
            os.mkdir(BASE)
            
        try:
            target = BASE + name + JSON
            with open(target, "w") as fp:
                json.dump(data, fp, indent=4)
            return True
        except:
            return False
    
    @staticmethod
    def clear_all():
        configs = [
            KakitanganConst.HOLIDAY_EVENT,
            KakitanganConst.COLLEAGUES,
            KakitanganConst.CALENDAR
        ]
        for config in configs:
            filename = BASE + config + JSON
            if os.path.isfile(filename):
                os.unlink(filename)
    
