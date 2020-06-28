import calendar
import datetime


def day_name_fun(time_name):
    new_calendar = datetime.datetime.strptime(time_name, '%m %d %Y').weekday()
    day_name = calendar.day_name[new_calendar]
    return day_name


if __name__ == '__main__':
    date_name = input()
    day_name_got = day_name_fun(date_name)
    print(day_name_got.upper())
