import json

import requests

BASE_URL = 'http://127.0.0.1:8000'
from datetime import date, datetime


def birthday(admin_id, group_id):
    today = date.today()
    url = f"{BASE_URL}/group/"
    user_url = f"{BASE_URL}/botuser/"
    user_response = requests.get(url=user_url).text
    user_data = json.loads(user_response)
    response = requests.get(url=url).text
    data = json.loads(response)
    have_group = False

    for i in data:

        if i['admin'] == admin_id:
            if i['id'] == group_id:
                have_group = True
    msg = ''
    if have_group == False:
        return "Sizda bundey guruh yo'q"
    else:
        len_user_data = len(user_data)
        count = 0
        for j in user_data:
            if j['group'] == group_id and j['admin']:
                user_birthday = datetime.strptime(j['birthday'], "%Y-%m-%d").date()
                next_birthday = datetime(today.year, user_birthday.month, user_birthday.day).date()
                if next_birthday < today:
                    next_birthday = datetime(today.year + 1, user_birthday.month, user_birthday.day).date()
                days_left = (next_birthday - today).days
                if days_left == 0:
                    msg += f"{j['first_name']} ning tug'ulgan kuni\n"
                else:
                    msg += f"{j['first_name']} ning tug'ulgan kuniga {days_left} kun qoldi\n"
            else:
                count += 1
    if count == len_user_data:
        return "bu guruhga hali odam qo'shmadingiz"
    return msg


