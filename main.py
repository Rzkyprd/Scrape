import requests
from bs4 import BeautifulSoup


headers = {
    'authority': 'www.cubetutor.com',
    'accept': '*/*',
    'x-requested-with': 'XMLHttpRequest',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://www.cubetutor.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.cubetutor.com/topcardsbyset/1',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': 'JSESSIONID=04D98BCDB4689887ACA8F9D426F6F505; _ga=GA1.2.562532548.1588005989; _gid=GA1.2.822785809.1588005989',
}

data = {
  't:ac': '1',
  't:formdata': 'byjWim5rtLJcD8P4BWZe94Mn6II=:H4sIAAAAAAAAAJWOPQ4BQRSAH4lCdBIRPe1oaKiQqEQkywHezj5rZOxM5j1/l3ECcQmFzh0cQKtS2DiARPsV3/edn1DaN6A+d36EIeHhMSLpMQmTJS0coOtCqtCjXpES9MQSjl2lXSBrYhUjkxrEOUQtY0M2aeaCrW8trpVH7fYuQmECFe0yCc5OcUMC1ckad9i2mKXtSILJ0v7BC5TzaPSN/v4Z/PszC04Tc7SNN4bZuOx6STrL1+leBDj4DxyMK0MBAQAA',
  'setSelect': 'BR',
  't:zoneid': 'topCardsZone'
}

def main():
    r = requests.post('https://www.cubetutor.com/topcardsbyset.topcardsform', 
                    headers=headers, data=data)
   
    content = (r.json()['content'])


    soup = BeautifulSoup(content, 'html.parser')

    cards = []

    for col in soup.find_all(class_='compareCubeColumn'):
        for line in col.get_text().split('\n')[1:]:
            parts = line.split(' ')
            occurence = parts[-1]
            name = " ".join(parts[1:-2])
 
            cards.append({'occurence': occurence, "name": name})

    print(cards)


if __name__ == "__main__": 
    main()