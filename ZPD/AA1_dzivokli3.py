import requests
from lxml import html
import json
import re
import os

output_dir = 'dzivoklu_data'
os.makedirs(output_dir, exist_ok=True)


def scrape_prices(base_url, total_pages, output_filename):
    one_time_purchase = []
    monthly = []
    daily = []

    # Loop through all pages
    for page_number in range(1, total_pages + 1):
        url = base_url.format(page_number)

        response = requests.get(url)

        if response.status_code == 200:
            tree = html.fromstring(response.content)

            listings_xpath = '//tr'

            listings_elements = tree.xpath(listings_xpath)

            for listing in listings_elements:
                # Extract price per m² and total price
                price_per_m2_element = listing.xpath('./td[9]/text()')
                price_per_m2_text = price_per_m2_element[0].strip() if price_per_m2_element else ""

                total_price_element = listing.xpath('./td[10]/text()')
                total_price_text = total_price_element[0].strip() if total_price_element else ""

                if "pērku" in listing.text_content():
                    continue

                # Clean prices
                cleaned_price_per_m2 = price_per_m2_text.strip()
                cleaned_total_price = total_price_text.strip()

                if cleaned_price_per_m2 and re.search(r'\d', cleaned_price_per_m2) and cleaned_total_price and re.search(r'\d', cleaned_total_price):
                    try:
                        # Convert to float
                        price_per_m2_value = float(re.sub(r'[^\d.]', '', cleaned_price_per_m2))
                        total_price_value = float(re.sub(r'[^\d.]', '', cleaned_total_price))

                        # Calculate size
                        size_value = total_price_value / price_per_m2_value if price_per_m2_value > 0 else 0

                        # Round values
                        size_value = round(size_value, 2)  # Change here for two decimal places
                        calculated_price = round(total_price_value, 2)

                        # Create a data dictionary
                        data_entry = {
                            "Price_per_m²": price_per_m2_value,
                            "Price": calculated_price,
                            "m²": size_value
                        }

                        # Categorize
                        pricing_type_element = listing.xpath('./td[10]/text()')
                        pricing_type_text = pricing_type_element[0].strip() if pricing_type_element else ""

                        if "/mēn." in pricing_type_text:
                            monthly.append(data_entry)
                        elif "dienā" in pricing_type_text:
                            daily.append(data_entry)
                        else:
                            one_time_purchase.append(data_entry)

                    except ValueError as e:
                        print(f"Skipping invalid price or size: Price_per_m²='{cleaned_price_per_m2}', Total_Price='{cleaned_total_price}'. Error: {e}")

        else:
            print(f"Failed to retrieve the webpage for page {page_number}. Status code: {response.status_code}")

    # Create a dictionary with lists of categorized prices
    sorted_prices = {
        "one_time_purchase": one_time_purchase,
        "monthly": monthly,
        "daily": daily
    }

    with open(os.path.join(output_dir, output_filename), 'w', encoding='utf-8') as json_file:
        json.dump(sorted_prices, json_file, ensure_ascii=False, indent=4, separators=(',', ': '))

    print(f"Data saved to {output_filename}:")
    print(json.dumps(sorted_prices, ensure_ascii=False, indent=4, separators=(',', ': ')))


locations = [
   {"name": "Centrs", "url": "https://www.ss.lv/lv/real-estate/flats/riga/centre/page{}.html", "archive_url": "https://www.ss.lv/lv/archive/real-estate/flats/riga/centre/page{}.html", "pages": 158},
    {"name": "Āgenskalns", "url": "https://www.ss.lv/lv/real-estate/flats/riga/agenskalns/page{}.html", "archive_url": "https://www.ss.lv/lv/archive/real-estate/flats/riga/agenskalns/page{}.html", "pages": 34},
    {"name": "Aplokciems", "url": "https://www.ss.lv/lv/real-estate/flats/riga/aplokciems/page{}.html", "archive_url": "https://www.ss.lv/lv/archive/real-estate/flats/riga/aplokciems/page{}.html", "pages": 1},
    {"name": "Berģi", "url": "https://www.ss.lv/lv/real-estate/flats/riga/bergi/page{}.html", "archive_url": "https://www.ss.lv/lv/archive/real-estate/flats/riga/bergi/page{}.html", "pages": 1},
    {"name": "Bieriņi", "url": "https://www.ss.lv/lv/real-estate/flats/riga/bierini/page{}.html", "archive_url": "https://www.ss.lv/lv/archive/real-estate/flats/riga/bierini/page{}.html", "pages": 2},
    {"name": "Bolderāja", "url": "https://www.ss.lv/lv/real-estate/flats/riga/bolderaya/page{}.html", "archive_url": "https://www.ss.lv/lv/archive/real-estate/flats/riga/bolderaya/page{}.html", "pages": 8},
    {"name": "Brekši", "url": "https://www.ss.lv/lv/real-estate/flats/riga/breksi/page{}.html", "archive_url": "https://www.ss.lv/lv/archive/real-estate/flats/riga/breksi/page{}.html", "pages": 2},
    {"name": "Čiekurkalns", "url": "https://www.ss.lv/lv/real-estate/flats/riga/chiekurkalns/page{}.html", "archive_url": "https://www.ss.lv/lv/archive/real-estate/flats/riga/chiekurkalns/page{}.html", "pages": 9},
    {"name": "Dārzciems", "url": "https://www.ss.lv/lv/real-estate/flats/riga/darzciems/page{}.html", "archive_url": "https://www.ss.lv/lv/archive/real-estate/flats/riga/darzciems/page{}.html", "pages": 10},

    {"name": "Daugavgrīva", "url": "https://www.ss.lv/lv/real-estate/flats/riga/daugavgriva/page{}.html", "archive_url": "https://www.ss.lv/lv/archive/real-estate/flats/riga/daugavgriva/page{}.html", "pages": 5},
    {"name": "Dreiliņi", "url": "https://www.ss.lv/lv/real-estate/flats/riga/dreilini/page{}.html", "archive_url": "https://www.ss.lv/lv/archive/real-estate/flats/riga/dreilini/page{}.html", "pages": 2},
    {"name": "Dzegužkalns", "url": "https://www.ss.lv/lv/real-estate/flats/riga/dzeguzhkalns/page{}.html", "archive_url": "https://www.ss.lv/lv/archive/real-estate/flats/riga/dzeguzhkalns/page{}.html", "pages": 8},
    {"name": "Grīziņkalns", "url": "https://www.ss.lv/lv/real-estate/flats/riga/grizinkalns/page{}.html", "archive_url": "https://www.ss.lv/lv/archive/real-estate/flats/riga/grizinkalns/page{}.html", "pages": 5},
    {"name": "Iļģuciems", "url": "https://www.ss.lv/lv/real-estate/flats/riga/ilguciems/page{}.html", "archive_url": "https://www.ss.lv/lv/archive/real-estate/flats/riga/ilguciems/page{}.html", "pages": 18},
    {"name": "Imanta", "url": "https://www.ss.lv/lv/real-estate/flats/riga/imanta/page{}.html", "archive_url": "https://www.ss.lv/lv/archive/real-estate/flats/riga/imanta/page{}.html", "pages": 29},
    {"name": "Jugla", "url": "https://www.ss.lv/lv/real-estate/flats/riga/yugla/page{}.html", "archive_url": "https://www.ss.lv/lv/archive/real-estate/flats/riga/yugla/page{}.html", "pages": 20},

    {"name": "Ķengarags", "url": "https://www.ss.lv/lv/real-estate/flats/riga/kengarags/page{}.html", "archive_url": "https://www.ss.lv/lv/archive/real-estate/flats/riga/kengarags/page{}.html", "pages": 36},
    {"name": "Ķīpsala", "url": "https://www.ss.lv/lv/real-estate/flats/riga/kipsala/page{}.html", "archive_url": "https://www.ss.lv/lv/archive/real-estate/flats/riga/kipsala/page{}.html", "pages": 2},

    {"name": "Klīversala", "url": "https://www.ss.lv/lv/real-estate/flats/riga/kliversala/page{}.html", "archive_url": "https://www.ss.lv/lv/archive/real-estate/flats/riga/kliversala/page{}.html", "pages": 4},
    {"name": "Krasta r-ns", "url": "https://www.ss.lv/lv/real-estate/flats/riga/krasta-st-area/page{}.html", "archive_url": "https://www.ss.lv/lv/archive/real-estate/flats/riga/krasta-st-area/page{}.html", "pages": 8},
    {"name": "Kundziņsala", "url": "https://www.ss.lv/lv/real-estate/flats/riga/kundzinsala/page{}.html", "archive_url": "https://www.ss.lv/lv/archive/real-estate/flats/riga/kundzinsala/page{}.html", "pages": 3},
    {"name": "Latgales priekšpilsēta", "url": "https://www.ss.lv/lv/real-estate/flats/riga/maskavas-priekshpilseta/page{}.html", "archive_url": "https://www.ss.lv/lv/archive/real-estate/flats/riga/maskavas-priekshpilseta/page{}.html", "pages": 13},
    {"name": "Mangaļi", "url": "https://www.ss.lv/lv/real-estate/flats/riga/mangali/page{}.html", "archive_url": "https://www.ss.lv/lv/archive/real-estate/flats/riga/mangali/page{}.html", "pages": 3},
    {"name": "Mangaļsala", "url": "https://www.ss.lv/lv/real-estate/flats/riga/mangalsala/page{}.html", "archive_url": "https://www.ss.lv/lv/archive/real-estate/flats/riga/mangalsala/page{}.html", "pages": 4},
    {"name": "Mežaparks", "url": "https://www.ss.lv/lv/real-estate/flats/riga/mezhapark/page{}.html", "archive_url": "https://www.ss.lv/lv/archive/real-estate/flats/riga/mezhapark/page{}.html", "pages": 8},
    {"name": "Mežciems", "url": "https://www.ss.lv/lv/real-estate/flats/riga/mezhciems/page{}.html", "archive_url": "https://www.ss.lv/lv/archive/real-estate/flats/riga/mezhciems/page{}.html", "pages": 15},
    {"name": "Pļavnieki", "url": "https://www.ss.lv/lv/real-estate/flats/riga/plyavnieki/page{}.html", "archive_url": "https://www.ss.lv/lv/archive/real-estate/flats/riga/plyavnieki/page{}.html", "pages": 31},
    {"name": "Purvciems", "url": "https://www.ss.lv/lv/real-estate/flats/riga/purvciems/page{}.html", "archive_url": "https://www.ss.lv/lv/archive/real-estate/flats/riga/purvciems/page{}.html", "pages": 48},

    {"name": "Šampēteris-Pleskodāle", "url": "https://www.ss.lv/lv/real-estate/flats/riga/shampeteris-pleskodale/page{}.html", "archive_url": "https://www.ss.lv/lv/archive/real-estate/flats/riga/shampeteris-pleskodale/page{}.html", "pages": 7},
    {"name": "Sarkandaugava", "url": "https://www.ss.lv/lv/real-estate/flats/riga/sarkandaugava/page{}.html", "archive_url": "https://www.ss.lv/lv/archive/real-estate/flats/riga/sarkandaugava/page{}.html", "pages": 15},
    {"name": "Šķirotava", "url": "https://www.ss.lv/lv/real-estate/flats/riga/shkirotava/page{}.html", "archive_url": "https://www.ss.lv/lv/archive/real-estate/flats/riga/shkirotava/page{}.html", "pages": 1},
    {"name": "Teika", "url": "https://www.ss.lv/lv/real-estate/flats/riga/teika/page{}.html", "archive_url": "https://www.ss.lv/lv/archive/real-estate/flats/riga/teika/page{}.html", "pages": 26},
    {"name": "Torņakalns", "url": "https://www.ss.lv/lv/real-estate/flats/riga/tornjakalns/page{}.html", "archive_url": "https://www.ss.lv/lv/archive/real-estate/flats/riga/tornjakalns/page{}.html", "pages": 6},


    
    {"name": "Vecmīlgrāvis", "url": "https://www.ss.lv/lv/real-estate/flats/riga/vecmilgravis/page{}.html", "archive_url": "https://www.ss.lv/lv/archive/real-estate/flats/riga/vecmilgravis/page{}.html", "pages": 12},
    {"name": "Vecrīga", "url": "https://www.ss.lv/lv/real-estate/flats/riga/vecriga/page{}.html", "archive_url": "https://www.ss.lv/lv/archive/real-estate/flats/riga/vecriga/page{}.html", "pages": 9},

    {"name": "Zasulauks", "url": "https://www.ss.lv/lv/real-estate/flats/riga/zasulauks/page{}.html", "archive_url": "https://www.ss.lv/lv/archive/real-estate/flats/riga/zasulauks/page{}.html", "pages": 1},
    {"name": "Ziepniekkalns", "url": "https://www.ss.lv/lv/real-estate/flats/riga/ziepniekkalns/page{}.html", "archive_url": "https://www.ss.lv/lv/archive/real-estate/flats/riga/ziepniekkalns/page{}.html", "pages": 22},
    {"name": "Zolitūde", "url": "https://www.ss.lv/lv/real-estate/flats/riga/zolitude/page{}.html", "archive_url": "https://www.ss.lv/lv/archive/real-estate/flats/riga/zolitude/page{}.html", "pages": 14},

    
    
    
]

# Loop through each location
for location in locations:
    # Scrape data from the original URL
    scrape_prices(location["url"], location["pages"], f"{location['name'].replace(' ', '_')}_prices.json")
    
    # Scrape data from the archive URL
    scrape_prices(location["archive_url"], location["pages"], f"archive_{location['name'].replace(' ', '_')}_prices.json")