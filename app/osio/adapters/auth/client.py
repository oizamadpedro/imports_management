import requests

class AuthClient:
    def userDetails(token):
        headers = {
            'Authorization': f'Bearer {token}'
        }
        response = requests.get("http://localhost:8080/auth/v1/user", headers=headers)
        return response.json()
    