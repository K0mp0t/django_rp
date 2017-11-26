import requests, bs4
def weath(city):
    s = requests.get('https://yandex.ru/pogoda/' +city)
    b = bs4.BeautifulSoup(s.text, "html.parser")
    temp__value = b.select('.temp__value')
    fact__condition = b.select('.fact__condition')
    temperature = temp__value[0].getText()
    conditions = fact__condition[0].getText()

    return temperature, conditions
