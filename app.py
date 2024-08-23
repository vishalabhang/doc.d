import streamlit as st
from streamlit_image_select import image_select

import requests
import json
import glob


Auth ='Basic dmlzaGFsYWJoYW5nNTVAeWFob28uY29t:gAW4HL5K7QXN1iZ7PBo3y'


def generateTalk():
    url = "https://api.d-id.com/talks"
    payload = json.dumps({
    "source_url": "https://raw.githubusercontent.com/vishalabhang/doc.d/master/avatar1.jpg",
    "script": {
        "type": "text",
        "input": "Hello world!"
    }
    })
    headers = {
    'Authorization': Auth,
    'Content-Type': 'application/json'
    }
    
    response = requests.request("POST", url, headers=headers, data=payload)


def main():
        
    st.header("Doc D integration Demo")
    images=glob.glob("input_images/*")
    select_image=image_select("Select Avatar",images)
    if select_image :
        print(select_image)
    



if __name__ == "__main__":
    main()

