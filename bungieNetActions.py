import requests
import json

# Uncomment line to print JSON output to a file:
# f = open("inventoryItem.txt", "w")


def transferItem(payload, session):
    req_string = base_url + "/TransferItem/"
    res = session.post(req_string, data=payload)
    error_stat = res.json()['ErrorStatus'].decode('utf-8')
    return res

def GetCurrentBungieAccount(session):
	req_string = 'https://www.bungie.net/Platform/User/GetCurrentBungieAccount/'
	res = session.get(req_string)
	print(req_string)
	error_state = res.json()['ErrorStatus'].decode('utf-8')
	print("Error status: " + error_state + "\n")

	return res