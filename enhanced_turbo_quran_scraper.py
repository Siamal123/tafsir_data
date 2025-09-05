import requests
import os
import time
import json

class EnhancedTurboQuranScraper:
    def __init__(self, base_url):
        self.base_url = base_url
        self.downloaded_files = []
        self.resume_file = 'resume.json'

    def load_progress(self):
        if os.path.exists(self.resume_file):
            with open(self.resume_file, 'r') as f:
                self.downloaded_files = json.load(f)

    def save_progress(self):
        with open(self.resume_file, 'w') as f:
            json.dump(self.downloaded_files, f)

    def download_data(self):
        # Example: Downloading data from different endpoints
        endpoints = ['endpoint1', 'endpoint2', 'endpoint3']
        for endpoint in endpoints:
            if endpoint not in self.downloaded_files:
                try:
                    response = requests.get(f"{self.base_url}/{endpoint}")
                    if response.status_code == 200:
                        with open(f"{endpoint}.json", 'w') as f:
                            f.write(response.text)
                        self.downloaded_files.append(endpoint)
                        self.save_progress()
                        print(f"Downloaded: {endpoint}")
                    else:
                        print(f"Failed to download: {endpoint} - Status code: {response.status_code}")
                except Exception as e:
                    print(f"Error downloading {endpoint}: {e}")
                    time.sleep(5)

    def run(self):
        self.load_progress()
        self.download_data()

if __name__ == "__main__":
    BASE_URL = "https://api.quran.com"
    scraper = EnhancedTurboQuranScraper(BASE_URL)
    scraper.run()