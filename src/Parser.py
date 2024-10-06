import requests
from bs4 import BeautifulSoup
from concurrent.futures import as_completed, ThreadPoolExecutor
from tqdm.asyncio import tqdm

class Parser:
    def __init__(self):
        self.urls = []

    def print_result(self):
        print(self.result)

    def get_internal_links(self, sitemap):
        page = requests.get(sitemap)
        soup = BeautifulSoup(page.content, 'xml')
        urls = soup.find_all('loc')

        for url in urls:
            currentURL = url.get_text()
            if currentURL.endswith(".xml"):
                self.get_internal_links(currentURL)
            else:
                self.urls.append(currentURL)

    def chunkify(self, lst, chunk_size): 
        for i in range(0, len(lst), chunk_size):
            yield lst[i:i + chunk_size]

    def process_url(self, url): 
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(response.text, 'lxml')

        return soup.body.get_text(' ', strip=True)

    def parse_sitemap(self, sitemap): 
        self.get_internal_links(sitemap)
        urls = self.urls
        
        num_workers = 10
        num_chunks = num_workers
        chunk_size = max(1, len(urls) // num_chunks)

        result = []

        for url in tqdm(urls, desc="Scraping data...", unit="url"):
            with ThreadPoolExecutor(max_workers=num_workers) as executor:
                futures = []
                chunks = self.chunkify(urls, chunk_size)

                for chunk in chunks:
                    futures.append(executor.submit(self.process_url, url))

                for future in as_completed(futures):
                    data = future.result()
                    result.append(data)

        return result

