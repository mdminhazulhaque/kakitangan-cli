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

import click
import tabulate

from kakitangan.auth import KakitanganAuth
from kakitangan.config import KakitanganConfig
from kakitangan.const import KakitanganConst
from kakitangan.filter import KakitanganFilter
from kakitangan.leave import KakitanganLeave
from kakitangan.aboutme import KakitanganAboutMe

@click.group()
def app():
    pass

@app.command(help="Login and save authorization token in disk")
@click.option('--username', '-u', 'username', required=True, type=str,
              help="Username or your company email address")
@click.option('--password', '-p', 'password', prompt=True, hide_input=True,
              help="Password, will not be stored",
              confirmation_prompt=False)
def login(username, password):
    success = KakitanganAuth(username, password)
    if success:
        print("Login success")
        exit(0)
    else:
        print("Failed logging in")
        exit(1)

@app.command(help="Logs out by clearing authorization token from disk")
@click.option('--confirm', '-y', is_flag=True,
              prompt='Confirm logout? [Y/N]', help="Confirm logout",)
def logout(confirm):
    if confirm or confirm.lower().startswith("y"):
        KakitanganConfig.clear_all()
        print("Logged out")
        exit(0)
    else:
        print("No action taken")
        exit(1)

@app.command(help="Fetches all calendar information from Kakitangan server")
def loadleaves():
    success = KakitanganLeave.loadleaves()
    if success:
        print("Updated leave database")
    else:
        print("An error occured")
    
@app.command(help="Shows personal information as Kakitangan user")
def aboutme():
    data = KakitanganAboutMe()
    if type(data) == list:
        print(tabulate.tabulate(data))
    else:
        print("An error occured")

@app.command(help="The user's leave statistics")
def myleavestat():
    data = KakitanganLeave.myleavestat()
    if type(data) == list:
        print(tabulate.tabulate(data))
    else:
        print("An error occured")
    
@app.command(help="Shows holidays")
@click.option('--all', '-a', is_flag=True, default=False,
              help="Shows past holidays also")
def holidays(all):
    data = KakitanganFilter.filter_calendar(KakitanganConst.HOLIDAY_EVENT,
                                            all=all)
    if type(data) == list:
        print(tabulate.tabulate(data))
    else:
        print("An error occured")
    
@app.command(help="Shows colleagues' leaves")
@click.option('--all', '-a', is_flag=True, default=False, help="Show past leaves also")
@click.option('--today', '-t', is_flag=True, default=False, help="Show leaves only on today")
@click.option('--untill', '-u', default=False, help="Show leaves upto date")
@click.option('--since', '-s', default=False, help="Show leaves from date")
@click.option('--date', '-d', default=False, help="Show leaves on specific date")
def colleagues(all, today, since, untill, date):
    data = KakitanganFilter.filter_calendar(KakitanganConst.COLLEAGUES,
                                            all=all,
                                            today=today,
                                            since=since,
                                            untill=untill,
                                            custom=date)
    if type(data) == list:
        print(tabulate.tabulate(data))
    else:
        print("An error occured")

@app.command(help="Shows user's leaves")
@click.option('--all', '-a', is_flag=True, default=False, help="Shows past leaves also")
def myleaves(all):
    data = KakitanganFilter.filter_calendar(KakitanganConst.CALENDAR,
                                            all=all)
    if type(data) == list:
        print(tabulate.tabulate(data))
    else:
        print("An error occured")

if __name__ == "__main__":
    app()
    
# TODO
# 'https://app.kakitangan.com/updates/check'
# 'https://app.kakitangan.com/leave/query_employees'
# 'https://app.kakitangan.com/leave/view_application?q=leave_history&start_date=27%2F04%2F2019&end_date=26%2F07%2F2019&_=1558924055891'
# 'https://app.kakitangan.com/leave/view_application?q=replacement_credit&start_date=27%2F04%2F2019&end_date=26%2F07%2F2019&_=1558924055892'
