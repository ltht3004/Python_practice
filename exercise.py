import requests
try:
    response = requests.get("https://jsonplaceholder.typicode.com/users", timeout=5)
    response.raise_for_status()
    data = response.json()
    for user in data:
        print("Name:", user["name"])
        print("Email:", user["email"])
except requests.RequestException as e:
    print(f"API call failed: {e}")
