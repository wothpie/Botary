import requests
import json

def get_external_ip():
    try:
        response = requests.get('https://api.ipify.org')
        return response.text
    except requests.RequestException as e:
        print("Hata:", e)
        return None

ip = get_external_ip()
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
url = "https://api.projectbo.com.tr/"

def GiveSDCP():
    try:
        with open("sdcp_data.json", "r") as file:
            data = json.load(file)
            return data["SDCP"]
    except Exception as e:
        print("Hata:", e)
        return None
    
SDCPs = GiveSDCP()

def GetBotaryTitle(cek, S232, S243):
    f = "GetBotaryTitle"
 
    response = requests.post(url, data={
        'func': f,
        'SDCP': SDCPs,
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

def GetBotaryContent(cek, S232, S243):
    f = "GetBotaryContent"

    response = requests.post(url, data={
        'func': f,
        'SDCP': SDCPs,
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

def GetBotaryOwner(cek, S232, S243):
    f = "GetBotaryOwner"

    response = requests.post(url, data={
        'func': f,
        'SDCP': SDCPs,
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
    
def GetBotaryInfo(cek, S232, S243):
    f = "GetBotaryInfo"

    response = requests.post(url, data={
        'func': f,
        'SDCP': SDCPs,
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

def GetBotaryPreview(cek, S232, S243):
    f = "GetBotaryPreview"

    response = requests.post(url, data={
        'func': f,
        'SDCP': SDCPs,
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
    
def GetBotaryDate(cek, S232, S243):
    f = "GetBotaryDate"

    response = requests.post(url, data={
        'func': f,
        'SDCP': SDCPs,
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
