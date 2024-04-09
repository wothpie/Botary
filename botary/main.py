import requests


def get_external_ip():
    try:
        response = requests.get('https://api.ipify.org')
        return response.text
    except requests.RequestException as e:
        print("Hata:", e)
        return None

ip = get_external_ip()

url = "https://api.projectbo.com.tr/"

def GetBotaryTitle(API, cek, S232, S243):
    f = "GetBotaryTitle"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    response = requests.post(url, data={
        'func': f,
        'API': API,
        'cek': cek,
         'ip' : ip,
        'S232': S232,
        'S243': S243
    }, headers=headers)

    if response.status_code == 200:
        return response.text
    else:
        print(f"Fonksiyon çağrısı başarısız oldu. Hata kodu: {response.status_code}")
        print(f"SDCP yanıtı: {response.text}")
        return None

def GetBotaryContent(API, cek, S232, S243):
    f = "GetBotaryContent"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    response = requests.post(url, data={
        'func': f,
        'API': API,
        'cek': cek,
         'ip' : ip,
        'S232': S232,
        'S243': S243
    }, headers=headers)

    if response.status_code == 200:
        return response.text
    else:
        print("Fonksiyon çağrısı başarısız oldu.")
        return None

def GetBotaryOwner(API, cek, S232, S243):
    f = "GetBotaryOwner"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    response = requests.post(url, data={
        'func': f,
        'API': API,
        'cek': cek,
         'ip' : ip,
        'S232': S232,
        'S243': S243
    }, headers=headers)

    if response.status_code == 200:
        return response.text
    else:
        print("Fonksiyon çağrısı başarısız oldu.")
        return None
