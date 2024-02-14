import os
try:
    import requests 
except:
    os.system('pip install requests')

while True:
    cc = input('Enter: ')

    headers = {
        'authority': 'beta.pickaxeproject.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6',
        'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryBCafTmVISFIOOVcQ',
        'origin': 'https://beta.pickaxeproject.com',
        'referer': 'https://beta.pickaxeproject.com/axe?id=Coder_RVII9',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
    }

    params = {
        'formid': 'Coder_RVII9',
        'embedded': 'false',
        'referrer': 'beta.pickaxeproject.com',
        'streamcapable': 'true',
        'uniqueid': '4JZO7I8FU5O39GC',
    }

    data = f'------WebKitFormBoundaryBCafTmVISFIOOVcQ\r\nContent-Disposition: form-data; name="id"\r\n\r\nCoder_RVII9\r\n------WebKitFormBoundaryBCafTmVISFIOOVcQ\r\nContent-Disposition: form-data; name="userinput:6cff5488-f159-4368-9569-c6f0dde48582"\r\n\r\n{cc}\r\n------WebKitFormBoundaryBCafTmVISFIOOVcQ--\r\n'.encode()

    response = requests.post(
        'https://beta.pickaxeproject.com/api/formsubmission',
        params=params,
        headers=headers,
        data=data,
    )

    cs = response.json().get('openaidata', '')

    headers = {
        'authority': 'streaming.pickaxeproject.com',
        'accept': '*/*',
        'accept-language': 'ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6',
        'content-type': 'text/plain;charset=UTF-8',
        'origin': 'https://beta.pickaxeproject.com',
        'referer': 'https://beta.pickaxeproject.com/',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
    }

    data = f'{{"id":"Coder_RVII9","data":"{cs}","host":"beta"}}'

    response = requests.post('https://streaming.pickaxeproject.com/api/streaming', headers=headers, data=data)
    print(response.text)
