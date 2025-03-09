import pandas as pd
import requests
from bs4 import BeautifulSoup

# URL to scrape
url = "https://www.launchgood.com/v4/campaign/ali_riazs_reformation_charity_ramadan_campaign_2025?src=internal_discover"

# Fetch the webpage
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Locate the specific div using its full class attribute
    target_div = soup.find("div", class_="text-2xl lg:text-5xl lg:font-semibold text-rebuild-primary lg:mb-2 font-bold me-1")
    
    if target_div: 
        content = target_div.get_text(strip=True)
        print("Scraped content:", content)
        
        spans = target_div.find_all("span")
        if len(spans) >= 0:
            number = spans[1].get_text(strip=True)
            print("Scraped number:", number)
        else:
            print("The expected span with the number was not found.")
    else:
        print("Target div not found.")
else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)


