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


def get_labs(token, url):
	api_call = "/v0/labs"
	url += api_call
	token = 'Bearer' + ' ' + token

	headers = {
		'accept': 'application/json',
		'Authorization': token
	}

	response = requests.get(url, headers=headers, verify=False).json()
	print("#" + " " + "Simulated labs on CML" + ": " + str(len(response)) + " at " + labname)
	return response


def get_labsdetail(token, url, labids):
	token = 'Bearer' + ' ' + token
	headers = {
		'accept': 'application/json',
		'Authorization': token
	}
	
	for labid in labids:
		api_call = "/v0/labs/" + labid
		laburl = url + api_call
		guiurl = url.rstrip('api')
		guiurl = guiurl + "lab/" + labid

		response = requests.get(laburl, headers=headers, verify=False).json()
		print("{0:42}{1:22}{2:18}{3:18}".
			format(str(response['lab_title']), str(response['created']), str(response['state']), str(guiurl)))


if __name__ == "__main__":
	auth_token = get_token(CML_URL, CML_USER, CML_PASS)
	print("#"*113)
	labids = get_labs(auth_token, CML_URL)
	print("#"*113)
	get_labsdetail(auth_token, CML_URL, labids)
	print("#"*113)