from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import csv
from datetime import datetime

def get_flight_data_to_csv(departure_airport, destination_airports, start_date, end_date):
    driver = webdriver.Chrome()
    flight_data = []

    for destination in destination_airports:
        url = f'https://www.kayak.fr/flights/{departure_airport}-{destination}/{start_date}/{end_date}?sort=bestflight_a'
        driver.get(url)
        wait = WebDriverWait(driver, 20)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='nrc6 nrc6-mod-pres-default']")))
        while True:
            try:
                more_results_button = driver.find_element_by_xpath("//div[@class='ULvh-button show-more-button']")
                more_results_button.click()
                wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='nrc6 nrc6-mod-pres-default']")))
            except:
                break
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')

        flights = soup.find_all(class_="nrc6 nrc6-mod-pres-default")

        for flight in flights:
            time_info = flight.find_all('div', class_='vmXl')
            departure_timex = time_info[0].text.strip() if time_info else "N/A"

            departure_time_parts = departure_timex.split(' – ')
            departure_time = departure_time_parts[0] if len(departure_time_parts) > 0 else "N/A"
            arrival_time = departure_time_parts[1] if len(departure_time_parts) > 1 else "N/A"


            departure_airport = departure_airport
            arrival_airport = destination

            flight_type = flight.find('div', class_='JWEO').text.strip()

            duration = flight.find('div', class_='xdW8').text.strip()

            airline_element = flight.find('div', class_='J0g6-labels-grp').find('div', class_='J0g6-operator-text')
            airline = airline_element.text.strip() if airline_element else "N/A"

            class_info_element = flight.find('div', class_='aC3z-option')
            class_info = class_info_element.text.strip() if class_info_element else "N/A"

            price_info = flight.find('div', class_='M_JD-large-display').text.strip()
            price_class_info = price_info.split('€')
            if len(price_class_info) >= 2:
                # Extracting price and class info
                price_str = price_class_info[0].replace('\xa0', '').strip()  # Remove non-breaking spaces
                class_info = price_class_info[1].strip()  # Extract class info
                price_str = ''.join(filter(str.isdigit, price_str))

                try:
                    price = float(price_str)
                except ValueError:
                    price = "N/A"
            else:
                price = "N/A"
                class_info = "N/A"

            choose_button = flight.find('a', class_='Iqt3-mod-bold')
            if choose_button:
                flight_partial_url = choose_button.get('href')
                flight_url = f"https://www.kayak.fr{flight_partial_url}"
            else:
                flight_url = "N/A"

            flight_data.append([departure_time, arrival_time, departure_airport, arrival_airport, flight_type, duration, airline, price, class_info, flight_url])

    driver.quit()

    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    unique_filename = f'flight_data_{timestamp}.csv'

    with open(unique_filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Departure Time', 'Arrival Time', 'Departure Airport', 'Arrival Airport', 'Flight Type', 'Duration', 'Airline', 'Price €', 'Class Info', 'Flight URL'])
        writer.writerows(flight_data)

departure_airport = "CMN"
destination_airports = ["PAR", "JFK","ROM","FRA","YYZ","IST","ABJ","ZRH","JED","LON","SYD"]
# "ROM","FRA","YYZ","IST","ABJ","ZRH","JED","LON","SYD"
start_date = "2024-04-26"
end_date = "2024-04-29"

get_flight_data_to_csv(departure_airport, destination_airports, start_date, end_date)
