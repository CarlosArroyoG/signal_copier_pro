import requests
from config import Config

class HotmartIntegration:
    @staticmethod
    def verify_purchase(transaction_code):
        url = "https://developers.hotmart.com/payments/api/v1/sales/verification"
        headers = {
            "Authorization": f"Bearer {HotmartIntegration.get_access_token()}",
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
        url = "https://api-sec-vlc.hotmart.com/security/oauth/token"
        data = {
            "grant_type": "client_credentials",
            "client_id": Config.HOTMART_APP_ID,
            "client_secret": Config.HOTMART_APP_SECRET
        }
        
        response = requests.post(url, data=data)
        
        if response.status_code == 200:
            return response.json()['access_token']
        return None