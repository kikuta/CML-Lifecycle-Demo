import json
import requests
import sys
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

	response = requests.request("POST", url, headers=headers, data=json.dumps(payload), verify=False)
	#print(response.text)
	return response.text.strip("\"")


def import_lab(token, url):
	labtitle = input("Please input an lab title [type q to quit]: ")

	api_call = "/v0/import"
	url += api_call + "?title=" + labtitle
	token = 'Bearer' + ' ' + token

	headers = {
		'Content-Type': 'application/json',
		'accept': 'application/json',
		'Authorization': token
	}

	args = sys.argv
	print(args[1])

	f = open(args[1])
	data = f.read()

	response = requests.request("POST", url, headers=headers, data=data, verify=False)
	print(response)


if __name__ == "__main__":
	auth_token = get_token(CML_URL, CML_USER, CML_PASS)
	import_lab(auth_token, CML_URL)