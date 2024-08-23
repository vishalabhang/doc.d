import requests


Reqdata={
    "source_url": "https://myhost.com/image.jpg",
    "script": {
        "type": "text",
        "input": "Hello world!"
    }
}
headers ={]}
requests.post(url="https://api.d-id.com/talks" ,data=Reqdata)
