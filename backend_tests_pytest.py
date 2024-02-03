# Salih Bora Öztürk
# ozturks19@itu.edu.tr

import requests

def test_flight_api_status_code():
    # Response'un HTTP durum kodunun 200 (OK) olduğunu kontrol eder.

    response = requests.get("https://flights-api.buraky.workers.dev/")
    assert response.status_code == 200

def test_flight_api_content_type_header():
    # Response'un 'Content-Type' başlığının 'application/json' olduğunu kontrol eder.

    response = requests.get("https://flights-api.buraky.workers.dev/")
    assert response.headers['Content-Type'] == "application/json"

def test_flight_api_response_structure():
    # Response'un JSON yapısının beklenen formatta olup olmadığını kontrol eder.

    response = requests.get("https://flights-api.buraky.workers.dev/")
    data = response.json()
    key = 'data'
    keys = ['id', 'from', 'to', 'date']
    assert type(data) == dict
    assert key in data
    assert type(data[key]) == list
    if len(data[key]) > 0:
        flights = data[key]
        assert all(all(k in flight for k in keys) for flight in flights)


