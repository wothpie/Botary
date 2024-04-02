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
def GetBotaryTitle(API,  cek, S232, S243):
    # HTTP isteği göndererek veriyi al
    
    f = "GetBotaryTitle"
    # POST isteği göndererek fonksiyonu çağır
    response = requests.post(url, data={
        'func' : f,
 
        'API': API, # API
        'ip' : ip,
        'cek': cek, # çekilecek verinin where'ini oluşturur
        'S232': S232, # kategori seçimi
        'S243': S243 # kod ile veri çekme
    })

    # Yanıtı kontrol et
    if response.status_code == 200:
        return response.text  # Yanıtı bir değişkene ata
    else:
        print("Fonksiyon çağrısı başarısız oldu.")
        return None


def GetBotaryContent(API,  cek, S232, S243):
    # HTTP isteği göndererek veriyi al
    
    f = "GetBotaryContent"
    # POST isteği göndererek fonksiyonu çağır
    response = requests.post(url, data={
        'func' : f,

        'API': API, # API
        'ip' : ip,
        'cek': cek, # çekilecek verinin where'ini oluşturur
        'S232': S232, # kategori seçimi
        'S243': S243 # kod ile veri çekme
    })

    # Yanıtı kontrol et
    if response.status_code == 200:
        return response.text  # Yanıtı bir değişkene ata
    else:
        print("Fonksiyon çağrısı başarısız oldu.")
        return None

def GetBotaryOwner(API, cek, S232, S243):
    # HTTP isteği göndererek veriyi al
    
    f = "GetBotaryOwner"
    # POST isteği göndererek fonksiyonu çağır
    response = requests.post(url, data={
        'func' : f,

        'API': API, # API
        'ip' : ip,
        'cek': cek, # çekilecek verinin where'ini oluşturur
        'S232': S232, # kategori seçimi
        'S243': S243 # kod ile veri çekme
    })

    # Yanıtı kontrol et
    if response.status_code == 200:
        return response.text  # Yanıtı bir değişkene ata
    else:
        print("Fonksiyon çağrısı başarısız oldu.")
        return None