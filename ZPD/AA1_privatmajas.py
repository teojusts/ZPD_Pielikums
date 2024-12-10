import requests
from lxml import html
import re
import json
import os

# List of base URLs for the pages you want to scrape
urls = {
    'centre': 'https://www.ss.lv/lv/real-estate/homes-summer-residences/riga/centre/',
    'agenskalns': 'https://www.ss.lv/lv/real-estate/homes-summer-residences/riga/agenskalns/',
    'bergi': 'https://www.ss.lv/lv/real-estate/homes-summer-residences/riga/bergi/',
    'bierini': 'https://www.ss.lv/lv/real-estate/homes-summer-residences/riga/bierini/',
    'bolderaya': 'https://www.ss.lv/lv/real-estate/homes-summer-residences/riga/bolderaya/',
    'bukulti': 'https://www.ss.lv/lv/real-estate/homes-summer-residences/riga/bukulti/',
    'chiekurkalns': 'https://www.ss.lv/lv/real-estate/homes-summer-residences/riga/chiekurkalns/',
    'darzciems': 'https://www.ss.lv/lv/real-estate/homes-summer-residences/riga/darzciems/',
    'darzini': 'https://www.ss.lv/lv/real-estate/homes-summer-residences/riga/darzini/',
    'dreilini': 'https://www.ss.lv/lv/real-estate/homes-summer-residences/riga/dreilini/',
    'dzeguzhkalns': 'https://www.ss.lv/lv/real-estate/homes-summer-residences/riga/dzeguzhkalns/',
    'ilguciems': 'https://www.ss.lv/lv/real-estate/homes-summer-residences/riga/ilguciems/',
    'imanta': 'https://www.ss.lv/lv/real-estate/homes-summer-residences/riga/imanta/',
    'yugla': 'https://www.ss.lv/lv/real-estate/homes-summer-residences/riga/yugla/',
    'jaunciems': 'https://www.ss.lv/lv/real-estate/homes-summer-residences/riga/jaunciems/',
    'kengarags': 'https://www.ss.lv/lv/real-estate/homes-summer-residences/riga/kengarags/',
    'krasta-st-area': 'https://www.ss.lv/lv/real-estate/homes-summer-residences/riga/krasta-st-area/',
    'maskavas-priekshpilseta': 'https://www.ss.lv/lv/real-estate/homes-summer-residences/riga/maskavas-priekshpilseta/',
    'mezhapark': 'https://www.ss.lv/lv/real-estate/homes-summer-residences/riga/mezhapark/',
    'mezhciems': 'https://www.ss.lv/lv/real-estate/homes-summer-residences/riga/mezhciems/',
    'plyavnieki': 'https://www.ss.lv/lv/real-estate/homes-summer-residences/riga/plyavnieki/',
    'purvciems': 'https://www.ss.lv/lv/real-estate/homes-summer-residences/riga/purvciems/',
    'shampeteris-pleskodale': 'https://www.ss.lv/lv/real-estate/homes-summer-residences/riga/shampeteris-pleskodale/',
    'sarkandaugava': 'https://www.ss.lv/lv/real-estate/homes-summer-residences/riga/sarkandaugava/',
    'teika': 'https://www.ss.lv/lv/real-estate/homes-summer-residences/riga/teika/',
    'tornjakalns': 'https://www.ss.lv/lv/real-estate/homes-summer-residences/riga/tornjakalns/',
    'vecmilgravis': 'https://www.ss.lv/lv/real-estate/homes-summer-residences/riga/vecmilgravis/',
    'vecriga': 'https://www.ss.lv/lv/real-estate/homes-summer-residences/riga/vecriga/',
    'ziepniekkalns': 'https://www.ss.lv/lv/real-estate/homes-summer-residences/riga/ziepniekkalns/',
    'zolitude': 'https://www.ss.lv/lv/real-estate/homes-summer-residences/riga/zolitude/'
}

# Ensure output directory exists
output_dir = 'real_estate_data'
os.makedirs(output_dir, exist_ok=True)

# Function to scrape and process data from a given URL
def scrape_and_process(url, region_name):
    response = requests.get(url)
    if response.status_code == 200:
        tree = html.fromstring(response.content)
        listings_xpath = '//tr[@id]'
        listings_elements = tree.xpath(listings_xpath)

        data = []
        for listing in listings_elements:
            price = listing.xpath('./td[9]/text()')
            price_text = price[0].strip() if price else 'Not found'

            price_per_m2 = listing.xpath('./td[8]/text()')
            price_per_m2_text = price_per_m2[0].strip() if price_per_m2 else 'Not found'

            # Skip if the listing is a rental or not for sale
            if any(word in price_text.lower() for word in ['pērku', 'mainu', 'maiņai', '/mēn']):
                continue

            price_cleaned = re.sub(r'[^\d]', '', price_text)
            price_per_m2_cleaned = re.sub(r'[^\d]', '', price_per_m2_text)

            if price_cleaned == '' or price_per_m2_cleaned == '':
                continue

            price_value = float(price_cleaned)
            m2_value = float(price_per_m2_cleaned)
            price_per_m2_value = round(price_value / m2_value, 2) if m2_value > 0 else 0

            data.append({
                "Price": price_value,
                "m²": m2_value,
                "Price_per_m²": price_per_m2_value
            })

        # Save data to a JSON file for the specific region
        file_name = os.path.join(output_dir, f'{region_name}_2.json')
        with open(file_name, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print(f"Data saved to {file_name}")
    else:
        print(f"Failed to retrieve the webpage {url}")

# Scrape data for each region
for region_name, base_url in urls.items():
    for page_number in range(1, 3):  # Assuming 2 pages per region
        url = f'{base_url}?page={page_number}'
        scrape_and_process(url, region_name)
