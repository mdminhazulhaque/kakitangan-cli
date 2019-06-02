[Kakitangan](https://www.kakitangan.com/platform.html) is an online HR Software for Malaysian businesses that helps handle payroll, claims, benefits, leave and more.

You can easily use the web version, or if you prefer, they have both [Android](https://play.google.com/store/apps/details?id=com.kakitangan&hl=en) and [iOS](https://itunes.apple.com/my/app/kakitangan/id1358869881) version too.

# Why CLI Version?

You can ask me why I made this CLI version although they have nice web and mobile version. Well, people like me prefers CLI than GUI. Also I wanted to learn how Python module works. So I decided to turn this into a pet project.

# Who Can Be Benefited From This

* If you are a project manager and need to frequently check who is on leave next week
* If you are a manager, you can get details who are on leave on a specific day before arranging any session
* If you are a simple developer, you can sniff on your colleagues and surprise them
* If you are a human resource person, you can get statistics on who makes the best use of leave policies

# Requirments

As written in Python3, the following modules are needed. Install using `pip3 install -r requirments.txt`

- [x] appdirs
- [x] click
- [x] tabulate

# Security?

I know. I know. You are damn worried about the security of your Kakitangan account. At least I am not going to store your password in plaintext like Google or Facebook did. <span style="color:red">This CLI app asks for your password once, tries to get a authorization token from Kakitangan API and ONLY saves the following things on your disk. It even asks for your password via stdin and hides the prompt so no trace is left in your bash history.</span>

* username
* sessionid
* authorizationtoken
* csrftoken

There is no way to get your password recovered from this 4 values.

# FAQ

* How does this app work?
    * The same way Kakitangan's web app works, using GET and POST requests to their API endpoints. Most of then returns JSON so I did not have to use parse HTML.
* Is there any API documentation for Kakitangan?
    * AFAIK, no. I had to trace their API calls via Chrome DevTools and figured out by myself how they work.
* Is this CLI app safe to use?
    * This app saves nothing but the sessionid and authorization token, same as your web browser does. It never stores the password.
* My question is not answered.
    * Send me email or post a new issue in this repository.

# How To Use It?

I am working hard to distribute it via `setuptools`. Before that, you can download the repo and execute the `kakitangan.py` as main file. The default commands are given below.

```
$ kakitangan.py --help
Usage: kakitangan.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  aboutme      Shows personal information as Kakitangan user
  colleagues   Shows colleagues' leaves
  holidays     Shows holidays
  loadleaves   Fetches all calendar information from Kakitangan server
  login        Login and save authorization token in disk
  logout       Logs out by clearing authorization token from disk
  myleaves     Shows user's leaves
  myleavestat  The user's leave statistics
```

First, you have to login, right? You have to pass the username/email via `-u` option. The password will be prompted and will be invisible as you type it. The password can also be passed via `-p` option but I tell you not to do so. Your password will be stored in `.bash_history` which would be a serious security issue.

```
$ kakitangan.py login -u john.doe@dream.job
Password: **********
Login success

$ kakitangan.py login -u john.doe@dream.job -u 1234567890
Login success
```

If your password is correct and you have internet connection, you are supposed to see the `Login success` message. Use the `aboutme` option to see your basic info.

```
$ kakitangan.py aboutme
---------------------  -------------------------------
Email                  john.doe@dream.job
Official Full Name     John Doe
Nationality            Bangladesh
Highest Qualification  Bachelors Degree
SOCSO Account          1234567890
Bank Account           1234567890
Bank Account Type      saving
Bank Account Name      AABBCCDD
Income Tax Account     1234567890
Salary                 1234567890
Preferred Name         John
Sex                    Male
Marital Status         married
Active                 True
Birth Date             1994-01-23
Phone                  1234567890
NRIC Number            1234567890
Passport Number        BB12345678
Employee ID            1000
Joined                 1970-01-01
Manager                boss@dream.job
Position               DevOps
Department             Tech
Location               Kuala Lumpur
---------------------  -------------------------------
```

That's enough for you I guess. Let's move to the leave calendar which is the best feature of Kakitangan. Before executing any calendar related command, you have to download the full calendar from Kakitangan server. `loadleaves` option will do it for you.

```
$ kakitangan.py loadleaves
Updated leave database
```

After doing so, you will find 3 new JSON files in `~/.config/kakitangan-cli` named `load_calendar.json`, `load_colleagues.json` and `load_holiday_event.json`. This 3 calendar holds data for yourself, your colleagues, and holidays respectively.

Now you are ready to get your colleagues' leave summary. The `colleagues` command takes several parameters.

```
Usage: kakitangan.py colleagues [OPTIONS]

  Shows colleagues' leaves

Options:
  -a, --all          Show past leaves also
  -t, --today        Show leaves only on today
  -u, --untill TEXT  Show leaves upto date
  -s, --since TEXT   Show leaves from date
  -d, --date TEXT    Show leaves on specific date
  --help             Show this message and exit.
```

By default, it will show leaves AFTER current date. You can see all leaves with `-a` parameter.

```
$ kakitangan.py colleagues
----------  --------------
2019-06-03  Abdul Doe
            Alice Begum
2019-06-04  Abdul Doe
            Charlie Ahmed
            Foo Bin Bar
            Alice Begum
2019-06-10  Foo Bin Bar
            Bob Mia
2019-06-11  Bob Mia
2019-06-12  Bob Mia
2019-06-13  Bob Mia
2019-06-14  Clara Khatun
            Bob Mia
2019-06-15  Clara Khatun
2019-06-16  Clara Khatun
2019-06-17  Clara Khatun
            Bob Mia
2019-06-18  Bob Mia
----------  --------------
```

It is possible to see who are on leave on a specific date. Just pass the date in `YYYY-MM-DD` format with `-d` parameter.

```
$ kakitangan.py colleagues -d 2019-06-10
----------  -----------
2019-06-10  Foo Bin Bar
            Bob Mia
----------  -----------
```

You might want to filter colleagues within specific date range. Just use the `-s` (since) and `-u` (until) parameter.

```
$ kakitangan.py colleagues -s 2019-06-15 -u 2019-06-17
----------  ------------
2019-06-15  Clara Khatun
2019-06-16  Clara Khatun
2019-06-17  Clara Khatun
            Bob Mia
----------  ------------
```

Similar to the leave calendar, you can check your holidays too. Use the `holidays` option for this purpose.

```
$ kakitangan.py holidays 
----------  ----------------------------
2019-06-05  Hari Raya Aidilfitri
2019-06-06  Hari Raya Aidilfitri Holiday
2019-08-11  Hari Raya Haji
2019-08-12  Hari Raya Haji
2019-08-31  Merdeka Day
2019-09-01  Awal Muharram
2019-09-02  Awal Muharram
2019-09-09  Agong's Birthday
2019-09-16  Malaysia Day
2019-10-27  Deepavali
2019-10-28  Deepavali
2019-11-09  Prophet Muhammad's birthday
2019-12-25  Christmas
----------  ----------------------------
```

As I said earlier, filtering hides old leaves/events. So you have to pass `-a` to see full holiday list.

```
$ kakitangan.py holidays -a
----------  ---------------------------------------------------------
2015-01-01  New Year
2015-01-02  New Year
2015-01-03  New Year
...
2017-06-25  Hari Raya Aidilfitri
2017-06-26  Hari Raya Aidilfitri
2017-06-27  Hari Raya Aidilfitri
...
2019-10-27  Deepavali
2019-10-28  Deepavali
2019-11-09  Prophet Muhammad's birthday
2019-12-25  Christmas
----------  ---------------------------------------------------------
```

Okay, you want to check your own leaves, right? You can! Use `myleaves` with `-a` parameter if you want to see the old leaves too.

```
$ kakitangan.py myleaves -a
----------  -----------
2019-02-28  Sick
2019-03-12  Sick
2019-03-21  Annual
2019-05-17  Annual (PM)
2019-05-21  Annual
2019-05-22  Annual
2019-05-23  Annual
2019-05-24  Annual
----------  -----------
```

If you need to know your leave statistics, I have added a command named `myleavestat`.

```
$ kakitangan.py myleavestat
-----------------------  -----------------
Compassionate            10/10
Annual                   25/50 (25 used)
Sick                     15/30 (15 used)
Paternity                10/10
Hospitalization          30/60 (30 used)
Replacement              1/1
Birthday Leave           1/1
Annual Leave Additional  5/5
CarryForward             5/5
Unpaid Leave             10/10
Bonus Leave              1/1
Exam/Study Leave         5/5
-----------------------  -----------------
```

Going back home? Don't want anyone sneak into your Kakitangan account? You can logout anytime. It's easy.

```
$ kakitangan.py logout
Confirm logout? [Y/N]: Y
Logged out
```

# TODO/BUGS

- [ ] Cases when internet is down is not handled yet
- [ ] Need to add logging feature to track file read/write events
- [ ] Need to add `Apply for Leave` feature
- [ ] Need to improve `loadleaves` command (remove manual invokation)
- [ ] You found one? Post as issue or send PR.
