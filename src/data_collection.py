from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from datetime import datetime
import time
import csv
import os
import boto3

# source URL for data
DATA_URL = 'https://safe.density.io/#/displays/dsp_956223069054042646?token=shr_o69HxjQ0BYrY2FPD9HxdirhJYcFDCeRolEd744Uj88e&share&qr'
# number of minutes to wait before recording each data entry
COLLECT_FREQ = 1
INTERVAL = 60
DIRECTORY = os.getcwd()
DATA_PATH = f'{DIRECTORY}/data'
START_TIME = 7
END_TIME = 23

def collect_data(num_data):
     """Collect NUM_DATA data entries from DATA_URL."""
     # set up headless browser
     chrome_options = Options()  
     chrome_options.add_argument("--headless")
     with Chrome(options=chrome_options) as browser:
          browser.get(DATA_URL)
          # wait for occupancy percentage to render
          WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'styles_fullness__rayxl')))
          # set number of data entries to collect
          data_num = 0
          while data_num < num_data:
               # get current time
               now = datetime.now()
               now_components = str(now).split()
               current_date = now_components[0]
               current_time = now_components[1]
               current_day = now.strftime('%A')

               # parse through HTML and grab data
               html = browser.page_source
               soup = BeautifulSoup(html, 'html.parser')
               div_container = soup.find('div', {'class':'styles_fullness__rayxl'})
               data_span = div_container.find('span')
               data = data_span.text.split('%')[0]
               # collect data based on day of the week
               data_row = {'date':current_date, 'time':current_time, 'day':current_day, 'occupancy':data}
               if not os.path.exists(DATA_PATH):
                    os.makedirs(DATA_PATH)
               append_data(f'{DATA_PATH}/{current_day.lower()}.csv', data_row)
               data_num += 1
               # pause program while not collecting data (collect data every COLLECT_FREQ minutes)
               if data_num < num_data:
                    time.sleep(COLLECT_FREQ * INTERVAL)
          
          # end session
          browser.close()
          browser.quit()

def append_data(filename, data_row):
     """Append DATA_ROW to FILENAME."""
     with open(filename, 'a', newline='') as file:
          writer = csv.DictWriter(file, fieldnames=data_row.keys())
          writer.writerow(data_row)

collect_data(100)