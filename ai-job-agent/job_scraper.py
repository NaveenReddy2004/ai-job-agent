import requests
from bs4 import BeautifulSoup

def scrape_jobs(query, num_results=5):
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"q": query, "hl": "en"}
    response = requests.get("https://www.google.com/search", params=params, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    results = []

    for g_card in soup.select(".tF2Cxc")[:num_results]:
        title = g_card.select_one("h3").text
        link = g_card.select_one("a")["href"]
        source = g_card.select_one(".VuuXrf").text if g_card.select_one(".VuuXrf") else "Unknown"
        results.append({
            "Job Title": title,
            "Company": source,
            "Job Link": link
        })
    return results