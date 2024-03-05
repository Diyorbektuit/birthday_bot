import requests
import json
BASE_URL = 'http://127.0.0.1:8000'


def take_admin_id(tg_id):
    url = f"{BASE_URL}/create_admin/"
    response = requests.get(url=url).text
    data = json.loads(response)
    for i in data:
        if i['tg_id'] == str(tg_id):
            return int(i['id'])


def create_admin(name, username, tg_id):
    url = f"{BASE_URL}/create_admin/"
    response = requests.get(url=url).text
    data = json.loads(response)
    have_admin = False
    for i in data:
        if i['tg_id'] == tg_id:
            have_admin = True
            break
    if have_admin == False:
        admin_post = requests.post(url=url, data={'name': name, 'username': username, 'tg_id': tg_id})
        return 'admin yaratildi'
    else:
        return 'Bunday admin mavjud'


def add_group_user(admin_id, group_id, position_id, tg_id, first_name, last_name, username, birthday):
    position_url = f"{BASE_URL}/position/"
    url = f"{BASE_URL}/botuser/"
    position_response = requests.get(url=position_url).text
    position_data = json.loads(position_response)
    response = requests.get(url=url).text
    data = json.loads(response)
    have_user_this_group = False
    is_admin = False
    for i in position_data:
        if i['id'] == position_id and i['group'] == group_id and i['admin'] == admin_id:
            is_admin = True
            break
    for j in data:
        if j['position'] == position_id and j['group'] == group_id and j['admin'] == admin_id and j['tg_id'] == tg_id:
            have_user_this_group = True
            break

    if is_admin == True and have_user_this_group == False:
        groupuser_post = requests.post(url=url, data={'admin': admin_id, 'group': group_id, 'position': position_id, 'tg_id': tg_id, 'first_name': first_name, 'last_name': last_name, 'username': username, 'birthday': birthday})
        return "user guruhga qo'shildi"

    if is_admin == False:
        return "siz bu guruhni admini emassiz yoki guruhingizda bunday lavozim yo'q"

    if have_user_this_group:
        return "bu guruhda allaqchon bu user mavjud"


def is_birthday(user, birthday, today):
    if birthday == today:
        return f"bugun {user}ni tug'ulgan kuni"


















