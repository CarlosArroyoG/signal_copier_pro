import requests
from config import HOTMART_API_URL, HOTMART_APP_ID, HOTMART_APP_SECRET

class HotmartChecker:
    @staticmethod
    def verify_purchase(transaction_code):
        url = f"{HOTMART_API_URL}/payments/api/v1/sales/verification"
        headers = {
            "Authorization": f"Bearer {HotmartChecker.get_access_token()}",
            "Content-Type": "application/json"
        }
        params = {
            "transaction_code": transaction_code
        }
        
        response = requests.get(url, headers=headers, params=params)
        
        if response.status_code == 200:
            return response.json()
        return None

    @staticmethod
    def get_access_token():
        url = f"{HOTMART_API_URL}/security/oauth/token"
        data = {
            "grant_type": "client_credentials",
            "client_id": HOTMART_APP_ID,
            "client_secret": HOTMART_APP_SECRET
        }
        
        response = requests.post(url, data=data)
        
        if response.status_code == 200:
            return response.json()['access_token']
        return None