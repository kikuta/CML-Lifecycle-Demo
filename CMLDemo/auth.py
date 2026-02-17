import json
import requests
import urllib3

import env_lab

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

CML_URL = env_lab.CML["host"]
CML_USER = env_lab.CML["username"]
CML_PASS = env_lab.CML["password"]


def get_token():
    url = 'https://{}/api/v0/authenticate'.format(CML_URL)

    headers = {
        'Content-Type': 'application/json',
        'accept': 'application/json'
    }

    payload = {
        "username": CML_USER,
        "password": CML_PASS
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload), verify=False)
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    token = get_token()
    print(token)