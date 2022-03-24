import requests

# serverless container
# url = "https://bbaunqhteq5ugp8kosu1.containers.yandexcloud.net/run/"

# local
url = "http://localhost:9999/run/"

headers = {
    "Content-Type": "application/json",
    # "Authorization": f"Api-Key {os.environ['API_KEY']}",
}

with open("payload.py") as f:
    main_content = f.read()

check_payload = {
    "files": [
        {
            "name": "main.py",
            "content": main_content,
        },
    ],
    "command": "python main.py",
}


resp = requests.post(url, headers=headers, json=check_payload)
print(resp)
print(resp.json()["stdout"])
print("\n__stderr__")
print(resp.json()["stderr"])
