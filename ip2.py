import requests

ip = requests.get('https://ip4.seeip.org/').text

api = "https://ipapi.co/"

url = api + ip + "/json"

json_data = requests.get(url).json()

details = [["IP Address", "Version", "City", "Postal Code", "Region", "Country", "ASN", "ISP",], 
        ["ip", "version", "city", "postal", "region", "country_name", "asn", "org"]]

for i in range(len(details[0])): 
    print(details[0][i] + ": " + json_data[details[1][i]])