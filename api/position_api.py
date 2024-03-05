import requests
import json
BASE_URL = 'http://127.0.0.1:8000'


def take_position_id(name):
    url = f"{BASE_URL}/position/"
    response = requests.get(url=url).text
    data = json.loads(response)
    for i in data:
        if i['name'] == name:
            return int(i['id'])


def group_position(group):
    url = f"{BASE_URL}/position/"
    response = requests.get(url=url).text
    data = json.loads(response)
    positions = []
    for i in data:
        if i['group'] == group:
            positions.append(i['name'])
    return positions


def create_position(admin_id, group_id, name):
    url = f"{BASE_URL}/position/"
    group_url = f"{BASE_URL}/group/"
    group_response = requests.get(url=group_url).text
    group_data = json.loads(group_response)
    response = requests.get(url=url).text
    data = json.loads(response)
    have_position = False
    is_admin = False
    for j in group_data:
        if j['admin'] == admin_id and j['id'] == group_id:
            is_admin = True

    for i in data:
        if i['admin'] == admin_id:
            if i['group'] == group_id:
                if i['name'] == name:
                    have_position = True
                    break

    if have_position == False and is_admin == True:
        position_post = requests.post(url=url, data={'admin': admin_id, 'group': group_id, 'name': name})
        return 'lavozim yaratildi'

    if is_admin == False:
        return 'Siz bu guruhni admini emassiz'

    if have_position == True:
        return 'Bu guruhda bunday lavozim allaqachon mavjud'