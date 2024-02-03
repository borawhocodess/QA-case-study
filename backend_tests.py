# Salih Bora Öztürk
# ozturks19@itu.edu.tr

import requests

def get_response(url):
    # Belirtilen URL'den HTTP GET isteği atar ve gelen yanıtı döndürür.

    return requests.get(url)

def check_status_code(response):
    # Response'un HTTP durum kodunun 200 (OK) olduğunu kontrol eder.
    # Eğer durum kodu 200 değilse AssertionError fırlatır.

    assert response.status_code == 200, "Status code should be 200."

def check_content_type(response):
    # Response'un 'Content-Type' başlığının 'application/json' olduğunu kontrol eder.
    # Eğer yanlışsa AssertionError fırlatır.

    assert response.headers['Content-Type'] == 'application/json', "Content-Type should be 'application/json'."

def check_response_structure(response):
    # Response'un JSON yapısının beklenen formatta olup olmadığını kontrol eder.
    # İlk 'data' sonrasında 'id', 'from', 'to', 'date' her bir uçuş objesinde mevcut mu diye bakar.
    # Eksik bir anahtar varsa AssertionError fırlatır.

    data = response.json()
    key = 'data'
    keys = ['id', 'from', 'to', 'date']
    assert key in data and all(all(k in flight for k in keys) for flight in data[key]), "Response structure is incorrect."

def run_tests(url):
    # API testlerini yapar ve sonuçları düzenli bir şekilde bastırır.

    print()
    print(f"Testing API: {url}")

    response = get_response(url)

    # API testlerinin isimleri ve fonksiyonları
    tests = {
        "Status Code Test": check_status_code,
        "Content-Type Test": check_content_type,
        "Response Structure Test": check_response_structure
    }

    max_length = max(len(test) for test in tests) + 1

    print('-' * max_length)

    for test, func in tests.items():
        try:
            func(response) # Test
            result = "PASSED"
        except AssertionError as error:
            result = f"FAILED: {error}"

        print(f"{test:<{max_length}} : {result}")

    print('-' * max_length)

    print("All tests completed.")
    print()

    return



# API tanımı ve testlerin çalıştırılması

API_URL = "https://flights-api.buraky.workers.dev/"
run_tests(API_URL)
