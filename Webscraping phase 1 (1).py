#!/usr/bin/env python
# coding: utf-8

# In[57]:


#  Webscraping the url of booking .com along 12 cities names provided 

import requests
from bs4 import BeautifulSoup

#  Create a list of cities
cities = ['Dubai', 'London', 'Kuala Lumpur', 'Manchester', 'Sydney', 'New Delhi', 'Birmingham', 'Berlin', 'Melbourne', 'Paris', 'Tokyo', 'Toronto']

# Create a function to scrape Booking.com URLs for each city
def scrape_booking_urls(city):
    search_query = f'Booking.com {city}'
    url = f'https://www.google.com/search?q={search_query}'
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find the first search result link
        results = soup.find_all('a')
        for result in results:
            if 'Booking.com' in result.get_text():
                return result['href']
    
    return None

# Create a dictionary to store the URLs for each city
city_urls = {}
for city in cities:
    url = scrape_booking_urls(city)
    city_urls[city] = url

# Print the dictionary with city names and their corresponding Booking.com URLs
for city, url in city_urls.items():
    print(f'{city}: {url}')


# In[ ]:




