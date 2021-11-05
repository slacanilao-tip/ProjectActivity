import requests         #import library

ip = requests.get('https://ip4.seeip.org/').text        #getting ip address of the device

api = "https://ipapi.co/"       #api that will be using

url = api + ip + "/json"        #using the json format of the api

json_data = requests.get(url).json()    #requesting json data from the api

details = [["IP Address", "Version", "City", "Postal Code", "Region", "Country", "ASN", "ISP",], 
        ["ip", "version", "city", "postal", "region", "country_name", "asn", "org"]]            #making an array for the details or field from the api

for i in range(len(details[0])): 
    print(details[0][i] + ": " + json_data[details[1][i]])      #printing the necessary details of the IP address