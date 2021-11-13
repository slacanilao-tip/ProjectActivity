from flask import Flask, json, render_template
import requests

#Getting IP Address of the device
ip = requests.get('https://ip4.seeip.org/').text

#Initializing the API
api = "https://ipapi.co/"

#Using the JSON format of the API
url = api + ip + "/json"

#Requesting for the JSON Data of the API
json_data = requests.get(url).json()

ip = json_data['ip']
version = json_data['version']
city = json_data['city']
postal_code = json_data['postal']
region = json_data['region']
country = json_data['country']
asn = json_data['asn']
isp = json_data['org']

sample = Flask('sample_app')

@sample.route("/")

def index():
    return render_template('index.html', html_ip = ip, html_version = version, html_city = city, html_postal = postal_code,
                            html_region = region, html_country = country, html_asn = asn, html_isp = isp)

if __name__ == '__main__':
    sample.run()