from playwright.sync_api import sync_playwright
import time
import pandas as pd

############## Initialise df ##################################################
df = pd.read_csv("ramadan25_input.csv")

# df = pd.DataFrame(data)
# Initialize the column with empty strings or None
df['donation_raised'] = None

############ Scrape function ################################################
def scrape_amount(input_url: str, full_name: str) -> str:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # Headless by default
        page = browser.new_page()
        
        url = input_url
        page.goto(url)

        # 💤 Wait for the element to appear
        amount_selector = "div.text-2xl.text-rebuild-primary.font-bold"
        page.wait_for_selector(amount_selector, timeout=10000)

        # Optional: wait extra time for animation if needed
        time.sleep(5)

        # 💰 Grab the amount text
        amount_text = page.locator(amount_selector).inner_text()
        print(f"💰 Scraped Amount: {amount_text}")

        browser.close()
        return amount_text

########### Run the scraper ############################################################
for i in range(0, len(df)):
    input_url = df['Fundraising link'][i]
    full_name = df.loc[i, 'Name']
    df['donation_raised'][i]=scrape_amount(input_url)
    print('[LOGGING] Loading next url....')