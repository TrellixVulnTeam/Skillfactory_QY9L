import requests
#import lxml.html
import json
#from lxml import etree
request = requests.get("https://api.exchangeratesapi.io/latest")
print(request.content)
data = json.loads(request.content)
#print(data['base'])
indexes = data['rates']
#print(indexes)
#for i in indexes:
    #print(i, indexes[i])
code = input(f"Введите код валюты, в которую вы хотите переконвертировать {data['base']}: ").upper()

amount = input("Введите кол-во исходной валюты: ")
print(f"Базовое значение {data['base']}, цена 1 {data['base']} в {code}: {indexes[code]}")
print(f"Для вашего случая: {amount} {data['base']} будет стоить {float(amount)*float(indexes[code])} {code}")
#tree = etree.parse(currency.content, lxml.html.HTMLParser())
#r = json.loads(currency.content)
#print(r)



#ul = tree.findall('body/div/div[3]/div/section/div[3]/div[1]/div/ul/li')
# создаём цикл в котором мы будем выводить название каждого элемента из списка
#for li in ul:
    #a = li.find('a')  # в каждом элементе находим где хранится заголовок новости. У нас это тег <a>. Т.е. гиперссылка на которую нужно нажать, чтобы перейти на страницу с новостью. (Гиперссылки в html это всегда тэг <a>)
    #time = li.find('time')
    #print(time.get('datetime'), a.text)
#    print(a.text) # из этого тега забираем текст - это и будет нашим названием
