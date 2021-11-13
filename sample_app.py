import requests #requests module allows us to send HTTP requests using Python
from flask import Flask, render_template, request

ip = requests.get('https://ip4.seeip.org/').content.decode('utf8') #getting the ip adress using api.ipify api

parsed_data = requests.get(f'https://ipapi.co/{ip}/json/').json() #using ipapi.co for the geolocation of the IP address

version = parsed_data['version']
city = parsed_data['city']
postal_code = parsed_data['postal']
region = parsed_data['region']
country = parsed_data['country_name']
isp = parsed_data['org']
asn = parsed_data['asn']

sample = Flask('sample_app')

@sample.route("/")

def index():
    return render_template('index.html', html_ip = ip, html_version = version, html_city = city, html_postal = postal_code,
                            html_region = region, html_country = country, html_asn = asn, html_isp = isp)

if __name__ == '__main__':
    sample.run(host="0.0.0.0", port=5000)