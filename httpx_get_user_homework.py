import httpx

login_payload = {
  "email": "user.booker@example.com",
  "password": "123456789"
}
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login",
                            json=login_payload)
login_response_data = login_response.json()
print("Login response:", login_response_data)
print("Status Code:", login_response.status_code)

access_token = login_response_data["token"]["accessToken"]

me_response = httpx.get("http://localhost:8000/api/v1/users/me",
                        headers={"Authorization": "Bearer " + access_token})
me_response_data = me_response.json()
print("User me:", me_response_data)
print("Status Code:", me_response.status_code)
