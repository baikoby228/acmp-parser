import requests
import fake_useragent
from bs4 import BeautifulSoup

URL = 'https://acmp.ru/index.asp'

def get_tests(id_task: int) -> list:
    user_agent = fake_useragent.UserAgent().random
    header = {'user-agent': user_agent}
    params = {
        'main': 'task',
        'id_task': id_task
    }

    response = requests.get(URL, params=params, headers=header)
    soup = BeautifulSoup(response.text, "lxml")
    #print(soup)

    table = soup.find('table', class_='main')
    rows = table.find_all('tr', class_='white2')

    res = []
    for row in rows:
        a = []
        for x in row.find_all('td')[1].stripped_strings:
            a.extend(x.split())
        for i in range(len(a)):
            try:
                a[i] = int(a[i])
            except ValueError:
                pass
        res.append(a)

    return res

if __name__ == '__main__':
    id_task = int(input())
    tests = get_tests(id_task)
    for test in tests:
        print(test)
