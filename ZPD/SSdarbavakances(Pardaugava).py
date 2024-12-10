from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import re
import json

# Initialize WebDriver
driver = webdriver.Chrome()  # Ensure chromedriver is installed and available

# Function to scrape price and address from a listing page
def scrape_price_and_address():
    try:
        # Locate the price element using the provided XPath
        price_xpath = "/html/body/div[3]/div/table/tbody/tr/td/div[1]/table/tbody/tr[1]/td/div[2]/div[1]"
        price_element = driver.find_element(By.XPATH, price_xpath)
        price_text = price_element.text.strip()

        # Search for price numbers after currency symbols like EUR, €, "EUR", "euro", etc.
        match = re.search(r"(\d{1,3}(?:[\s,]?\d{3})*(?:[\.,]?\d+)?(?:\s*(EUR|€|eiro|e?uro|\se?ur|\s?€))?(/h)?)", price_text, re.IGNORECASE)
        price = match.group(1) if match else None

        # Locate the address element using the provided XPath
        address_xpath = "/html/body/div[3]/div/table/tbody/tr/td/div[1]/table/tbody/tr[1]/td/div[2]/div[1]/table/tbody/tr/td[2]/table/tbody/tr[4]/td[2]"
        address_element = driver.find_element(By.XPATH, address_xpath)
        address = address_element.text.strip()

        # Clean the address to remove "iela" and "gatve"
        address = re.sub(r'\b(iela|gatve)\b', '', address, flags=re.IGNORECASE).strip()

        return price, address
    except Exception as e:
        print("Error scraping price or address:", e)
    return None, None

# Function to scroll down to an element to make sure it's visible
def scroll_to_element(element):
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    time.sleep(1)  # Wait for the page to adjust after scrolling

# Function to scrape listings from the current page
def scrape_listings():
    listing_rows = driver.find_elements(By.XPATH, "/html/body/div[4]/div/table/tbody/tr/td/div[1]/table/tbody/tr/td/form/table[2]/tbody/tr")
    data = []

    # Iterate through the listings starting from tr[2] to tr[n]
    for row_index in range(2, len(listing_rows) + 2):  # Start from 2 and go up to n
        try:
            # Dynamically build the XPath for the listing based on row_index
            listing_link_xpath = f"/html/body/div[4]/div/table/tbody/tr/td/div[1]/table/tbody/tr/td/form/table[2]/tbody/tr[{row_index}]"
            
            # Find the listing link element
            listing_link = driver.find_element(By.XPATH, listing_link_xpath)

            # Scroll to the listing to ensure it's in view
            scroll_to_element(listing_link)

            # Click the current listing's link
            ActionChains(driver).move_to_element(listing_link).click().perform()

            # Wait for the page to load
            time.sleep(2)

            # Scrape price and address from the listing page
            price, address = scrape_price_and_address()
            if price and address:
                print(f"Listing {row_index - 1}: Found price: {price} EUR, Address: {address}")
                data.append({"price": price, "address": address})

            # Go back to the main list of listings
            driver.back()

            # Wait for the main page to load again
            time.sleep(2)

        except Exception as e:
            print(f"Error with listing {row_index}: {e}")
            continue

    return data

# Function to perform the selection and typing actions on the base page
def perform_initial_selections():
    try:
        # 1. Click the button at the provided XPath
        button_xpath = "/html/body/div[4]/div/table/tbody/tr/td/div[1]/table/tbody/tr/td/form/table/tbody/tr/td[2]/input"
        driver.find_element(By.XPATH, button_xpath).click()
        time.sleep(1)  # Wait for the page to respond

        # 2. Click the first dropdown to select and type "r"
        dropdown_xpath_1 = "/html/body/div[4]/div/table/tbody/tr/td/div[1]/table/tbody/tr/td/form/table[1]/tbody/tr/td[1]/table/tbody/tr/td[2]/span/select"
        dropdown_element_1 = driver.find_element(By.XPATH, dropdown_xpath_1)
        ActionChains(driver).move_to_element(dropdown_element_1).click().perform()
        dropdown_element_1.send_keys("r")
        dropdown_element_1.send_keys(Keys.RETURN)
        time.sleep(2)  # Wait for the action to complete

        # 3. Click the second dropdown to select and type "pardaugava"
        dropdown_xpath_2 = "/html/body/div[4]/div/table/tbody/tr/td/div[1]/table/tbody/tr/td/form/table[1]/tbody/tr/td[1]/table/tbody/tr/td[2]/select"
        dropdown_element_2 = driver.find_element(By.XPATH, dropdown_xpath_2)
        ActionChains(driver).move_to_element(dropdown_element_2).click().perform()
        dropdown_element_2.send_keys("pardaugava")
        dropdown_element_2.send_keys(Keys.RETURN)
        time.sleep(2)  # Wait for the action to complete

    except Exception as e:
        print("Error performing initial selections:", e)

# Function to go to the next page
def go_to_next_page(page_number):
    try:
        url = f"https://www.ss.lv/lv/work/are-required/filter/page{page_number}.html"
        driver.get(url)
        time.sleep(3)  # Wait for the page to load
        print(f"Scraping page {page_number}...")
    except Exception as e:
        print(f"Error going to page {page_number}: {e}")

# Main function to handle pagination and scraping
def scrape_all_pages(start_page=1, max_pages=4):
    all_data = []

    # First scrape the base page without the page number
    print("Opening and selecting options on the base page...")
    driver.get("https://www.ss.lv/lv/work/are-required/filter/")  # First page URL (no page number)
    time.sleep(3)  # Wait for the page to load

    # Perform the initial selections (type 'r' and 'pardaugava')
    perform_initial_selections()

    # Now scrape the listings from the first page
    print("Scraping first page...")
    page_data = scrape_listings()
    all_data.extend(page_data)

    # Now scrape additional pages
    for page_number in range(2, max_pages + 1):
        go_to_next_page(page_number)

        # Scrape the listings on the current page
        page_data = scrape_listings()
        all_data.extend(page_data)

        # Check if there are no listings or it's the last page
        if not page_data:
            print(f"No more listings on page {page_number}.")
            break

    # Save the collected data to a JSON file with Latvian letters
    with open("pardaugava_vakances.json", "w", encoding="utf-8") as f:
        json.dump(all_data, f, ensure_ascii=False, indent=4)

    # Print all collected data from all pages
    print("Collected data:", all_data)
    return all_data

# Initialize the browser and start scraping from the first page
driver = webdriver.Chrome()  # Ensure chromedriver is installed and available
all_data = scrape_all_pages(start_page=1, max_pages=3)  # Adjust the max_pages if necessary

# Close the browser
driver.quit()
