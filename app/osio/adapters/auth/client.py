import requests
import httpx


class AuthClient:
    async def userDetails(token):
        headers = {
            'Authorization': f'Bearer {token}'
        }
        async with httpx.AsyncClient() as client:
            response = await client.get("http://localhost:8080/auth/v1/user", headers=headers)
            return response.json()
    