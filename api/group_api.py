import requests
import json
BASE_URL = 'http://127.0.0.1:8000'


def take_group_id(name):
    url = f"{BASE_URL}/group/"
    response = requests.get(url=url).text
    data = json.loads(response)
    for i in data:
        if i['name'] == name:
            return int(i['id'])


def user_groups(user_id):
    url = f"{BASE_URL}/group/"
    response = requests.get(url=url).text
    data = json.loads(response)
    groups = []
    for i in data:
        if i['admin'] == user_id:
            groups.append(i['name'])
    return groups





def create_group(admin_id, name):
    url = f"{BASE_URL}/group/"
    response = requests.get(url=url).text
    data = json.loads(response)
    have_group = False
    for i in data:
        if i['admin'] == admin_id and i['name'] == name:
            have_group = True
            break

    if have_group == False:
        group_post = requests.post(url=url, data={'admin': admin_id, 'name': name})
        return 'guruh yaratildi'
    else:
        return 'sizda bunday guruh mavjud'