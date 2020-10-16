from bs4 import BeautifulSoup
from urllib import request


class Scraper:
    def __init__(self, site):
        self.url = site

    def scrape(self):
        response = request.urlopen(self.url)
        content = response.read()
        parser = "html.parser"
        bs = BeautifulSoup(content, parser)
        l = bs.find_all("a")
        # print(l)
        for tag in l:
            url = tag.get("href")
            if url is None:
                continue
            if "html" in url:
                print("\n" + url)


if __name__ == "__main__":
    url = "http://news.baidu.com/"
    S = Scraper(url)
    S.scrape()
