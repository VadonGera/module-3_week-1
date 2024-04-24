import requests
import json
import datetime as dt

FORMAT_DATE = '%Y-%m-%d'


def format_date(date_str: str, my_format: str = FORMAT_DATE) -> dt.datetime:
    try:
        return dt.datetime.strptime(date_str, my_format)
    except:
        return dt.datetime.now()


my_data = {
    "avatar": "https://static.wikia.nocookie.net/rustarwars/images/f/f0/George_lucas.jpg",
    "birth": "1944-05-14",
    "name": "George Lucas",
    "state": 1_000_000
}

URL = 'https://66095c000f324a9a28832d7e.mockapi.io/users'

# response = requests.post(url=URL, json=my_data)
# print(response.status_code)

response = requests.get(url=URL)
print(response.status_code)
data = response.json()

count = 0
condition_76 = 0
id_wilson = 0
my_state = 1_000_000.99
my_date = dt.datetime.now()
birth_april = 0
old_user = ''
poor_user = ''

for item in data:
    if item['name'] == 'Wilson VonRueden':
        id_wilson = int(item['id'])
        # print(json.dumps(item, ensure_ascii=False, sort_keys=True, indent=4))
    if count < 76:
        count += 1
        condition_76 += float(item['state'])
    if format_date(item['birth'][:10]) < my_date:
        my_date = format_date(item['birth'][:10])
        old_user = item['name'], item['birth']
    if item['state'] == '1.000.000':
        state = 1_000_000.00
    else:
        state = float(item['state'])
    if state < my_state:
        my_state = state
        poor_user = item['name'], item['state']
    if f"{format_date(item['birth'][:10]).month:02d}" == '04':
        birth_april += 1

    if item['name'] == 'George Lucas':
        my_data = item

print(f'ID пользователя "Wilson VonRueden": {id_wilson}')
print(f'Состояние первых 76 пользователей: {condition_76}')
print(f'Имя самого старого пользователя: {old_user[0]}, birth: {old_user[1]}')
print(f'Имя самого бедного пользователя: {poor_user[0]}, state: {poor_user[1]}')
print(f'В апреле родилось пользователей: {birth_april}')
print(f'То, что загрузил через "requests.post(url=URL, json=my_data)":')
print(json.dumps(my_data, ensure_ascii=False, sort_keys=True, indent=4))
