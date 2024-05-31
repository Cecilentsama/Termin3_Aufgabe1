from datetime import date


def age_from_date(date: date):
    today = date.today()
    ret = today.year - date.year
    if (today.month, today.day) < (date.month, date.day):
        ret -= 1
    return ret
