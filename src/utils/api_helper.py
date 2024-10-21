import requests
from src.configs.configs_api import Config
from src.utils.logger import Logger

class APIHelper:
    def __init__(self):
        self.base_url = Config.BASE_URL
        self.headers = Config.HEADERS
        self.timeout = Config.TIMEOUT
        self.logger = Logger.get_logger()
        self.session = requests.Session()
    
    def get(self, endpoint, params=None):
        url = f"{self.base_url}{endpoint}"
        self.logger.info(f"Making GET request to: {url}")
        response = self.session.get(
            url,
            headers=self.headers,
            params=params,
            timeout=self.timeout
        )
        self.logger.info(f"Response Status Code: {response.status_code}")
        return response
    
    def post(self, endpoint, payload):
        url = f"{self.base_url}{endpoint}"
        self.logger.info(f"Making POST request to: {url}")
        self.logger.info(f"Request Payload: {payload}")
        response = self.session.post(
            url,
            headers=self.headers,
            json=payload,
            timeout=self.timeout
        )
        self.logger.info(f"Response Status Code: {response.status_code}")
        return response
    
    def put(self, endpoint, payload):
        url = f"{self.base_url}{endpoint}"
        self.logger.info(f"Making PUT request to: {url}")
        self.logger.info(f"Request Payload: {payload}")
        response = self.session.put(
            url,
            headers=self.headers,
            json=payload,
            timeout=self.timeout
        )
        self.logger.info(f"Response Status Code: {response.status_code}")
        return response
    
    def delete(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        self.logger.info(f"Making DELETE request to: {url}")
        response = self.session.delete(
            url,
            headers=self.headers,
            timeout=self.timeout
        )
        self.logger.info(f"Response Status Code: {response.status_code}")
        return response