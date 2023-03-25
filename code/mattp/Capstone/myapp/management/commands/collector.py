from django.core.management.base import BaseCommand
from django.utils import timezone
import logging
import json
import requests
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Scrapes fish species data from FishMap.org and saves it to a JSON file'

    # def add_arguments(self, parser):
    #     parser.add_argument('zip_codes', nargs='+', type=str, help='One or more zip codes to scrape data for')

    # def handle(self, *args, **options):
    #     zip_codes = options['zip_codes']
    #     logger.info('Starting FishMap scraper at {}'.format(timezone.now()))

    
    #     service = Service('/Users/Downloads/chromedriver_mac_arm64/chromedriver') # Optional argument, identify location of chromedriver
    #     service.start()
    #     driver = webdriver.Remote(service.service_url)  

    #     for zip_code in zip_codes:
    #         logger.info('Scraping data for zip code {}'.format(zip_code))

            
    #         driver.get('http://www.fishmap.org/')
            
    #         search_box = driver.find_element('name', 'zip')
    #         search_box.send_keys(zip_code)
    #         search_box.submit()

            
    #         with open('./data/fishmap_' + zip_code + '.html', 'w') as f:
    #             data = BeautifulSoup(driver.page_source, 'html.parser')
    #             logger.debug('HTML content for zip code {}: {}'.format(zip_code, data))
    #             urls = data.find_all('a')
    #             reg = re.compile('\/species')
    #             species_list = []
    #             for url in urls:
    #                 if reg.search(str(url)):
    #                     species_name = url['href'].replace('.html', '').replace('/species/', '').replace('-', ' ')
    #                     if all(c.isalpha() or c == '-' or c.isspace() for c in species_name):
    #                         species_list.append(species_name)
    #             f.write(driver.page_source)

            
    #         with open('species_list.txt', 'a') as f:
    #             f.write('\n'.join(species_list) + '\n')

            
    #         try:
    #             with open('species_data.json', 'r') as f:
    #                 existing_data = json.load(f)
    #         except FileNotFoundError:
    #             existing_data = {}

    #         if zip_code in existing_data:
    #             existing_data[zip_code].extend(species_list)
    #         else:
    #             existing_data[zip_code] = species_list

    #         with open('species_data.json', 'w') as f:
    #             json.dump(existing_data, f)

        
    #     driver.quit()

    #     # Save fish data to JSON file
    #     try:
    #         with open('species_data.json', 'r') as f:
    #             species_data = json.load(f)
    #     except FileNotFoundError:
    #         species_data = {}

    #     try:
    #         with open('fishes.json', 'r') as f:
    #             fishes_data = json.load(f)
    #     except FileNotFoundError:
    #         fishes_data = {}

    #     for zip_code, species_list in species_data.items():
    #         for species in species_list:
    #             if species in fishes_data:
    #                 if zip_code not in fishes_data[species]:
    #                     fishes_data[species].append(zip_code)
    #             else:
    #                 fishes_data[species] = [zip_code]

    #     with open('fishes.json', 'w') as f:
    #         json.dump(fishes_data, f)

    #     logger.info('FishMap scraper completed')
    
    def handle(self, *args, **options):
        # Your code goes here
        # Selenium
        service = Service('/Users/Downloads/chromedriver_mac_arm64/chromedriver') # Optional argument, identify location of chromedriver
        service.start()
        driver = webdriver.Remote(service.service_url)  
        # Go to fishmap.org
        driver.get('http://www.fishmap.org/')
        # delay browser response
        time.sleep(5)
        # Find the input named zip
        search_box = driver.find_element('name', 'zip')
        zip_codes = '97232'
        # zip_codes = ['97200', '972001']
        search_box.send_keys(zip_codes)
        search_box.submit()
        # Use the current pages url to create request
        # response = requests.get(driver.current_url)
        # Print response
        # print(response.text)
        #Save response to file
        with open('./data/fishmap_' + zip_codes + '.html', 'a') as f:
            data = BeautifulSoup(driver.page_source, 'html.parser')
            print(data)
            results = {
                "name": data.urls,
            }
            urls = data.find_all('a')
            reg = re.compile('\/species')
            found = []
            print(found)
            for url in urls:
                if reg.search(str(url)):
                    found.append(url.text)
            f.write(driver.page_source)
        print(driver.page_source)
        time.sleep(5) # delay browser response
        driver.quit()
        # # Beautiful Soup

        # # with open('./data/fishmap_97035.html', 'w') as f:
        # #     data = BeautifulSoup(f, 'html.parser')
        # #     urls = data.find_all('a')
        # #     reg = re.compile('\/species')
        # #     for url in urls:
        # #         if reg.search(str(url)):
        # #             print(url.text)

        # print("success!")

        #######################################################################################


        with open(f"./data/fishmap_{zip_codes}.html") as f:
            html_doc = f.read()

        soup = BeautifulSoup(html_doc, 'html.parser')


        species_links = []
        for link in soup.find_all('a'):
            href = link.get('href')
            if href and '/species/' in href:
                species_links.append(href)


        species_list = []
        for link in species_links:
            species_name = link.replace('.html', '').replace('/species/', '')
        
            if all(c.isalpha() or c == '-' for c in species_name):
                
                species_name = species_name.replace('-', ' ')
                species_list.append(species_name)


        with open("./data/species_list.txt", "w") as f:
            f.write("\n".join(species_list))


        print("The list of species has been saved to species_list.txt")


        species_dict = {zip_codes: species_list}

        # # Read the existing species data from the JSON file, if it exists
        # try:
        #     with open("species_data.json", "r") as f:
        #         existing_data = json.load(f)
        # except FileNotFoundError:
        #     existing_data = {}

        # # Merge the new species data with the existing data
        # existing_data.update(species_dict)

        # # Write the merged data to the JSON file
        # with open("species_data.json", "w") as f:
        #     json.dump(existing_data, f)
        # Read the existing species data from the JSON file, if it exists
        try:
            with open("./data/species_data.json", "r") as f:
                existing_data = json.load(f)
        except FileNotFoundError:
            existing_data = {}


        if zip_codes in existing_data:
            existing_data[zip_codes].extend(species_list)
        else:
            existing_data[zip_codes] = species_list


        with open("./data/species_data.json", "w") as f:
            json.dump(existing_data, f)
            
        ######################################################################

        with open("./data/species_data.json", "r") as f:
            species_data = json.load(f)

        try:
            with open("./data/fishes.json", "r") as f:
                fishes_data = json.load(f)
        except FileNotFoundError:
            fishes_data = {}

        for zip_code, species_list in species_data.items():
            for species in species_list:
                
                if species in fishes_data:
                    
                    if zip_code not in fishes_data[species]:
                        fishes_data[species].append(zip_code)
                else:
                    
                    fishes_data[species] = [zip_code]


        with open("./data/fishes.json", "w") as f:
            json.dump(fishes_data, f)


        print("DONE!!!")