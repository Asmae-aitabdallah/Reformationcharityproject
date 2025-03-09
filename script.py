from bs4 import BeautifulSoup
# from requests_html import HTMLSession

print("test")

url = "https://www.launchgood.com/v4/campaign/ali_riazs_reformation_charity_ramadan_campaign_2025?src=internal_discover"

def get_website_content():
    session = HTMLSession()
    try:
        r = session.get(url)
        r.html.render(sleep=2)
        soup = BeautifulSoup(r.html.html, 'html.parser')
        return soup
    except Exception as e:
        print("Error fetching the website:", e)
        return None

def get_div_content():
    soup = get_website_content()
    if soup:
        div = soup.select_one("div.text-2xl.lg\\:text-5xl.lg\\:font-semibold.text-rebuild-primary.lg\\:mb-2.font-bold.me-1")
        return div
    return None

def main():
    div_content = get_div_content()
    if div_content:
        spans = div_content.find_all("span")
        span_texts = [span.get_text(strip=True) for span in spans]
        result_string = "".join(span_texts)
        print("Resulting string:", result_string)
    else:
        print("The specified div was not found.")

if __name__ == '__main__':
    main()
