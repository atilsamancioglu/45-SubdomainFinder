import requests

def request(url):
	try:
		return requests.get("http://" + url)
	except requests.exceptions.ConnectionError:
		pass

targetUrl = "google.com"

with open("subdomainlist.txt","r") as listFile:
	for line in listFile:
		word = line.strip()
		testUrl = word + "." + targetUrl
		response = request(testUrl)
		if response:
			print ("Found subdomain --> "+testUrl)
		
