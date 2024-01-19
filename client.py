import requests


response = requests.get(
    "http://127.0.0.1:5000/upscaling/9f0e858f-ac73-4ff5-bc73-e286dc441d76",
    # files={
    # 'file': open('lama_300px.png', 'rb'),}
    )

print(response.status_code)
print(response.text)