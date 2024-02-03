# Salih Bora Öztürk
# ozturks19@itu.edu.tr

from playwright.sync_api import sync_playwright

def click_and_collect_options(xpath, page):
    # Dropdown menüsünden şehir ve havalimanı seçeneklerini toplayan fonksiyon.
    # Belirtilen XPath'e göre dropdown menüsünü açar.
    # Açılan menüdeki tüm seçenekleri toplar.
    # Şehir isimleri ve havalimanı kodları için bir liste oluşturur.
    # Dropdown menüsünü kapatmak için sayfanın dışına tıklar.

    page.click(xpath)
    dropdown_options = page.query_selector_all(f"{xpath}/../ul/li")

    city_airport_pairs = [(option.query_selector("span:first-child").text_content().strip(),
                           option.query_selector("span.ml-2").text_content().strip())
                          for option in dropdown_options]

    page.click("body")

    return city_airport_pairs

def search_for_flights(page, from_city, to_city, from_input_xpath, to_input_xpath):
    # Verilen kalkış ve varış noktaları ile uçuş arama işlemini gerçekleştiren fonksiyon.
    # Kalkış şehri bilgisini doldurur ve enter tuşuna basar.
    # Varış şehri bilgisini doldurur ve enter tuşuna basar.

    page.fill(from_input_xpath, from_city)
    page.keyboard.press('Enter')
    page.fill(to_input_xpath, to_city)
    page.keyboard.press('Enter')

def is_flight_available(page, no_flights_selector, no_flights_text):
    # Seçilen rota için uçuş bulunup bulunmadığını kontrol eden fonksiyon.
    # Belirtilen seçicideki metnin içerisinde verilen mesajın bulunup bulunmadığını kontrol eder.

    return no_flights_text not in page.text_content(no_flights_selector)

def report_flight_search_results(from_airport, to_airport, flights_found, page):
    # Uçuş arama sonuçlarını ekrana yazdıran fonksiyon.
    # Eğer uçuş bulunmuşsa, bulunan ve listelenen uçuş sayısını raporlar.
    # Bulunan ve listelenen uçuş sayılarının eşleşip eşleşmediğini kontrol eder.
    # Eğer uçuş bulunamamışsa, uçuş olmadığını yazdırır.

    if flights_found:
        found_items_text = page.text_content("p.mb-10")
        found_items_count = int(found_items_text.split(' ')[1])
        listed_items_count = page.locator("ul[role='list'] li").count()
        assert found_items_count == listed_items_count, f"Mismatch: found {found_items_count}, listed {listed_items_count}."
        print(f"{from_airport} -> {to_airport}: found {found_items_count} flights, {listed_items_count} items listed.")
    else:
        print(f"{from_airport} -> {to_airport}: No flights available.")
    print("-" * 10)

def perform_flight_search_tests():
    # Uçuş arama işlevlerini test eden ana fonksiyon.
    # Tarayıcıyı başlatır.
    # Test edilecek web sayfasını açar.
    # Form elemanlarının XPath'lerini içerir.
    # Uçuş bulunamadığında gösterilen mesajı ve seçicisini içerir.
    # Kalkış ve varış noktaları için seçenekleri toplar.
    # Kalkış ve varış noktaları için tüm kombinasyonları test eder.
    # Kalkış ve varış noktaları aynıysa uyarı verir.
    # Değilse uçuş araması yapar ve sonuçları raporlar.
    # Tarayıcıyı kapatır.

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://flights-app.pages.dev/")

        xpaths = {
            "from_input": "//*[@id='headlessui-combobox-input-:Rq9lla:']",
            "to_input": "//*[@id='headlessui-combobox-input-:Rqhlla:']",
            "from_button": "//*[@id='headlessui-combobox-button-:R1a9lla:']",
            "to_button": "//*[@id='headlessui-combobox-button-:R1ahlla:']"
        }

        no_flights_text = "Bu iki şehir arasında uçuş bulunmuyor. Başka iki şehir seçmeyi deneyebilirsiniz."
        no_flights_selector = "div.mt-24"

        from_options = click_and_collect_options(xpaths["from_button"], page)
        to_options = click_and_collect_options(xpaths["to_button"], page)

        for from_city, from_airport in from_options:
            for to_city, to_airport in to_options:
                if from_city == to_city:
                    print(f"{from_airport} -> {to_airport}: Skipping search. Departure and destination cities cannot be the same.")
                    print("-" * 10)
                    continue

                search_for_flights(page, from_city, to_city, xpaths["from_input"], xpaths["to_input"])
                flights_found = is_flight_available(page, no_flights_selector, no_flights_text)
                report_flight_search_results(from_airport, to_airport, flights_found, page)

        browser.close()

if __name__ == "__main__":
    perform_flight_search_tests()
