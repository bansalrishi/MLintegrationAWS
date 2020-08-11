import requests
import json
ip_address = "13.232.117.125"
port = "5000"
data = [[5.1, 3.5, 1.5, 0.3]]

url = 'http://{0}:{1}/predict/'.format(ip_address, port)

json_data = json.dumps(data)
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
response = requests.post(url, data=json_data, headers=headers)
print(response, response.text)