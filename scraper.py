import requests
from bs4 import BeautifulSoup

def scrape_anime(query):
    url = f"https://myanimelist.net/anime.php?q={query}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    results = []
    for item in soup.select(".seasonal-anime.js-seasonal-anime"):
        title = item.select_one(".title .link-title")
        link = title["href"] if title else None
        name = title.get_text(strip=True) if title else "Unknown"
        if name and link:
            results.append({"title": name, "link": link})

    if not results:
        for item in soup.select("a.hoverinfo_trigger.fw-b.fl-l"):
            name = item.get_text(strip=True)
            link = item["href"]
            results.append({"title": name, "link": link})

    return results
