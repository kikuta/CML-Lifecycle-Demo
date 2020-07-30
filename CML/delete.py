import json
import requests
import urllib3

import env_lab

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

CML_URL = "https://" + env_lab.CML["host"] + "/api"
CML_USER = env_lab.CML["username"]
CML_PASS = env_lab.CML["password"]

labname = "CML Lab " + env_lab.CML["host"]


def get_token(url, user, password):
	api_call = "/v0/authenticate"
	url += api_call

	headers = {
		'Content-Type': 'application/json',
		'accept': 'application/json'
	}

	payload = {
		"username": user,
		"password": password
	}

	response = requests.request("POST", url, headers=headers, data=json.dumps(payload), verify=False).json()
	return response

def delete_lab(token, url):
    token = 'Bearer' + ' ' + token
    headers = {
		'accept': 'application/json',
		'Authorization': token
	}

    deletelabid = input("Please input lab ID to be deleted? [type q to quit]: ")

    api_call = "/v0/labs/" + deletelabid
    url = url + api_call
    
    response = requests.delete(url, headers=headers, verify=False)
    print(response)

if __name__ == "__main__":
    auth_token = get_token(CML_URL, CML_USER, CML_PASS)
    delete_lab(auth_token, CML_URL)