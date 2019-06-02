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

from .urls import KakitanganURLS
from .headers import KakitanganHeaders
from .config import KakitanganConfig

import requests
import json

def KakitanganAboutMe():
    try:
        config = KakitanganConfig.load("authorization")
        headers = KakitanganHeaders.json()
        headers['authorization'] = 'Token ' + config['ATK']
        response = requests.get(KakitanganURLS.USER + config['username'], headers=headers)
        content = response.text\
            .replace("'", "\"")\
            .replace("True", "true")\
            .replace("False", "false")
        j = json.loads(content)
        data = [
            ["Email", j["email"]],
            ["Official Full Name", j["official_full_name"]],
            ["Nationality", j["nationality"]],
            ["Highest Qualification", j["personals"]["highest_qualification"]],
            ["SOCSO Account", j["personals"]["socso_acc"]],
            ["Bank Account", j["personals"]["bank"]["account"]],
            ["Bank Account Type", j["personals"]["bank"]["type"]],
            ["Bank Account Name", j["personals"]["bank"]["name"]],
            ["Income Tax Account", j["personals"]["income_tax_acc"]],
            ["Salary", j["pay_rate"]["salary"]],
            ["Preferred Name", j["preferred_name"]],
            ["Sex", "Male" if j["sex"] == "M" else "Female"],
            ["Marital Status", j["marital"]],
            ["Active", j["is_active"]],
            ["Birth Date", j["birth_date"]],
            ["Phone", j["phone"]],
            ["NRIC Number", j["nric"]],
            ["Passport Number", j["passport"]],
            ["Employee ID", j["employee_id"]],
            ["Joined", j["joined_time"]],
            ["Manager", j["manager"]],
            ["Position", j["position"]],
            ["Department", j["department"]],
            ["Location", j["location"]]
        ]
        return data
    except:
        return False
