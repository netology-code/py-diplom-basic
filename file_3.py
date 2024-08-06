from abc import update_abstractmethods
import requests
import json
import time

# API Constants - ideally load these from environment variables
# APP_ID = '837974821'
TOKEN = 'vk1.a.-JoIfPWTQzyYOiL4Xdma7zZ_ZLY6LaYHMs5-Wf41ByZ9UDHxHk2foQGWkLiuOKVbjR-PcRuP3nuBY6TuYzcxY5l0AXINnOdT5AOVu1Qqn4RgfXb_qwzruHNzK01xdLgDrmSluaEfeeAUZCxtgZ_IizpLa4qTaTOx1W0bNbeBtqhwJGEB2N15eG4kQWwSXoee'
class VKAPIClient:
    """Represents a VK API client."""
    API_BASE_URL = 'https://api.vk.com/method'
    RATE_LIMIT = 3 # API calls per second
    def __init__(self, token, user_id):
        """Initializes the VK client with access token, user ID, and version."""
        self.token = token
        self.id = user_id
        self.last_call_time = 0
    def get_common_params(self):
        """Retrieves common parameters for all API requests."""
        return {'access_token': self.token, 'v': '5.131'}
    def rate_limit(self):
        """Enforces rate limiting for API calls."""
        current_time = time.time()
        if current_time - self.last_call_time < 1 / self.RATE_LIMIT:
            time.sleep(1 / self.RATE_LIMIT - (current_time - self.last_call_time))
        self.last_call_time = current_time
    def get_status(self):
        """Retrieves user status information from VK API."""
        self.rate_limit()
        params = self.get_common_params()
        params.update({'user_id': self.id})
        try:
            response = requests.get(f'{self.API_BASE_URL}/status.get', params=params)
            response.raise_for_status() # Raise an exception for bad status codes
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching status: {e}")
            return None
            
if __name__ == '__main__':
    user_id = input("Enter user ID: ")
    vk_client = VKAPIClient(TOKEN, user_id)
    status = vk_client.get_status()
    if status:
        print(status)