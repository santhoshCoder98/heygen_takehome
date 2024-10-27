import requests
import time

class VideoTranslationClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_status(self):
        response = requests.get(f"{self.base_url}/status")
        if response.status_code == 200:
            return response.json()['result']
        else:
            raise Exception("Error fetching status")

    def check_status(self, interval=2, timeout=30):
        start_time = time.time()
        while time.time() - start_time < timeout:
            status = self.get_status()
            print(f"Status: {status}")
            if status == "completed":
                print("Video translation completed successfully.")
                return
            elif status == "error":
                print("Error occurred during translation.")
                return
            time.sleep(interval)

if __name__ == "__main__":
    client = VideoTranslationClient("http://localhost:8000")
    client.check_status()
