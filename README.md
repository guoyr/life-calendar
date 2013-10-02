life-calendar
=============

a calendar for every month of your life

How to use
==========

OS X:
0. change the numbers in data.txt to be your current age in month and year. So 1 23 would be 23 years and 1 month.
1. run `crontab -e` and enter the following `0 0 1 * * /usr/bin/python path_to_cron.py`