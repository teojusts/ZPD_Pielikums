from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import re
import json

# Set up Chrome options
options = Options()
options.add_argument('--disable-logging')  # Suppress unnecessary logs
options.add_argument('--start-maximized')  # Open browser maximized

# Initialize WebDriver with options
driver = webdriver.Chrome(options=options)

try:
    # Open the desired webpage
    url = "https://cvvp.nva.gov.lv/#/pub/vakances/saraksts#eyJvZmZzZXQiOjM2NzIsImxpbWl0IjoyNSwicGFnZVkiOjI2ODYxNn0%253D"
    driver.get(url)
    print("Opened the URL successfully.")

    # Adjust wait time as necessary
    wait = WebDriverWait(driver, 30)

    # Scroll down to load all rows dynamically
    print("Loading all rows...")
    for _ in range(50):  # Adjust the range as needed
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)  # Pause to allow content to load

    print("Rows loaded. Starting data extraction...")

    # Initialize a list to store extracted data
    location_wage_data = []

    # Define the list of phrases to exclude
    exclude_phrases = ["darbs objektos", "Rīgas iela", "Rīgas rajons", "Latvijas teritorija", "Ogre"]

    # Define XPath for all rows
    rows_xpath = '/html/body/div[2]/div/div/div/div/div/div/div[2]/table/tbody[1]/tr'

    # Wait for all rows to be present
    rows = wait.until(EC.presence_of_all_elements_located((By.XPATH, rows_xpath)))

    # Iterate over rows and extract data
    for row_num, row in enumerate(rows, start=1):
        try:
            # Construct the XPath dynamically for the wage and location
            wage_xpath = f'{rows_xpath}[{row_num}]/td[4]/a/span'
            location_xpath = f'{rows_xpath}[{row_num}]/td[3]/a/span'

            # Wait for and extract the wage and location
            wage_element = wait.until(EC.presence_of_element_located((By.XPATH, wage_xpath)))
            location_element = wait.until(EC.presence_of_element_located((By.XPATH, location_xpath)))

            # Extract text content
            wage_text = wage_element.text
            location_text = location_element.text

            # Skip locations with the excluded phrases
            if any(exclude_phrase in location_text for exclude_phrase in exclude_phrases):
                continue  # Skip this entry if it contains any of the excluded phrases

            # Only process locations containing "Rīga"
            if "Rīga" in location_text:
                # Remove "iela" and "gatve" from the location text
                location_cleaned = re.sub(r"\b(iela|gatve)\b", "", location_text).strip()

                numbers = re.findall(r'\d+', wage_text)  # Extract all numeric values from the wage text
                if numbers:
                    wage_value = int(numbers[0])  # Get the first number (wage)

                    # Handle wages under 200
                    if wage_value < 170:
                        adjusted_wage = wage_value * 160  # Convert hourly wage to monthly
                        location_wage_data.append({"location": location_cleaned, "wage": adjusted_wage})

                    # Skip wages between 200 and 700
                    elif wage_value >= 700:
                        location_wage_data.append({"location": location_cleaned, "wage": wage_value})

        except Exception as e:
            print(f"Row {row_num} skipped due to error: {e}")

    # Save the data to a JSON file
    with open("location_wage_data_riga_filtered.json", "w", encoding="utf-8") as json_file:
        json.dump(location_wage_data, json_file, ensure_ascii=False, indent=4)

    print("Data successfully saved to 'location_wage_data_riga_filtered.json'.")

    # Pause to observe the action
    time.sleep(5)  # Optional: Wait to ensure actions are complete

except Exception as e:
    print(f"Error: {e}")
    driver.save_screenshot("error_screenshot.png")  # Capture a screenshot if there’s an error
finally:
    driver.quit()
